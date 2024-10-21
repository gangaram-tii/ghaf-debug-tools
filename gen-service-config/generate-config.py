import time
import os
import caps
import syscalls
from baseconfig import baseConfig
import extraconfs
import sh
import re
import sys
import argparse

class SystemdService:
    def __init__(self, service):
        override_dir = f"/run/systemd/system/{service}.d"
        self.config_path = os.path.join(override_dir, "override.conf")
        self.service = service
        self.initial_configs = sh.systemctl("cat", service).splitlines()
        sh.sudo("mkdir", "-p", override_dir)

    def initial_config_value(self, config):
        for line in self.initial_configs:
            if config in line:
                #print(f"Found in initial config: {line.strip()}")
                return line.strip()
        return None

    def is_active(self):
        try:
            res = sh.systemctl('is-active', self.service)
            return res.strip() == 'active'
        except sh.ErrorReturnCode as e:
            return False

    def start(self):
        return sh.sudo('systemctl', 'start', self.service)

    def stop_service(self):
        return sh.sudo('systemctl', 'stop', self.service)

    def reload(self):
        try:
            sh.sudo('systemctl', 'daemon-reload')
            if self.is_active():
                sh.sudo('systemctl', 'restart', self.service)
            else:
                sh.sudo('systemctl', 'start', self.service)
            return True

        except sh.ErrorReturnCode as e:
            return False

    def reset(self):
        sh.sudo("rm", "-rf", self.config_path)
        self.reload()

    def get_name(self) -> str:
        return self.service

    def get_config_path(self) -> str:
        return self.config_path

    def get_exposure(self) -> float:
        out = sh.systemd_analyze("security", self.service)
        lines = out.splitlines()
        # Get the last line
        last_line = lines[-1] if lines else None
        match = re.search(r"(\d+\.\d+)", last_line)
        if match:
            number = match.group(1)
            return float(number)
        else:
            return float(-1.0)


def generate_base_hardened_config(service: SystemdService) -> list[str]:
    hardenedconfigs = ["[Service]"]
    for conf, possible_values in baseConfig.items():
        initial_conf = service.initial_config_value(conf)
        if initial_conf is not None:
            #print("\tFound in service config")
            # Initial configs can not be overridden
            hardenedconfigs.append(initial_conf)
            print(f"{initial_conf}".ljust(50)+"[✓]")
            continue
        else:
            for val in possible_values:
                buffer = "\n".join(hardenedconfigs)
                buffer += f"\n{conf}={val}"
                print(f"{conf}={val}".ljust(50), end="")

                # Writing to a text file
                with open(service.get_config_path(), 'w') as file:
                    file.write(buffer)
                if service.reload() == False:
                    print("[✗]")
                    service.reset()
                    continue
                time.sleep(6)
                if service.is_active():
                    hardenedconfigs.append(f"{conf}={val}")
                    print("[✓]")
                    break
                else:
                    print("[✗]")
                    service.reset()

    return hardenedconfigs

def check_sudo():
    if os.geteuid() != 0:
        print("This program must be run as root (use sudo).")
        sys.exit(1)

def main():
    check_sudo()
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate hardened configuration for service.')
    parser.add_argument('service', type=str, help='Name of the service')
    parser.add_argument('output', type=str, help='Output file path to save hardened configuration')

    # Parse the command-line arguments
    args = parser.parse_args()

    service = SystemdService(args.service)
    old_exposure = service.get_exposure()
    base_hardened_configs = generate_base_hardened_config(service)
    hardened_configs = "\n".join(base_hardened_configs)
    with open(args.output, 'w') as file:
        file.write(hardened_configs)
    new_exposure = service.get_exposure()
    print(f"Exposure level before: [{old_exposure}] and after: [{new_exposure}]")

if __name__ == "__main__":
    main()
