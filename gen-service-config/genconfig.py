import subprocess
import time
import os
import caps
import syscalls
from baseconfig import baseConfig
import extraconfs
import sh

SERVICE_NAME = 'your_service_name'  # Replace with your service name

def read_service_config(service_name: str):
    # Define the path to the runtime override configuration file
    override_dir = f"/run/systemd/system/{service_name}.d"
    override_file_path = os.path.join(override_dir, "override.conf")

    # Step 1: Run the `systemctl edit --runtime` to ensure the override file is created
    try:
        subprocess.run(['systemctl', 'edit', '--runtime', service_name], check=True)

        # Step 2: Read the existing content of the override.conf into a buffer
        if os.path.exists(override_file_path):
            with open(override_file_path, 'r') as override_file:
                override_content = override_file.readlines()
                #print(f"Existing override content for {service_name}:\n{''.join(override_content)}")
                return override_content
        else:
            print(f"No override file found for {service_name}.")
            return None

    except subprocess.CalledProcessError as e:
        print(f"Error running systemctl command: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def find_pattern_in_service_config(content, pattern):
    if content is not None:
        for line in content:
            if pattern in line:
                #print(f"Found matching line: {line.strip()}")
                return line.strip()
        #print(f"No matching line found for pattern '{pattern}'.")
    return None

def is_service_active(service_name):
    try:
        result = subprocess.run(
            ['systemctl', 'is-active', service_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        print(f"Service status: {result.stdout}")
        return result.stdout.strip() == 'active'
    except subprocess.CalledProcessError:
        return False

def start_service(service_name):
    subprocess.run(['sudo', 'systemctl', 'start', service_name], check=False)

def stop_service(service_name):
    subprocess.run(['sudo','systemctl', 'stop', service_name], check=True)

def reload_systemd():
    subprocess.run(['sudo', 'systemctl', 'daemon-reload'], check=True)

def custom_task():
    # Add your custom task here
    print("Performing custom task...")

def main():
    service_name = "bluetooth.service"
    serviceconfig = read_service_config(service_name)
    overrideconfig = ["[Service]"]
    for conf, vals in baseConfig.items():
        print(f"Processing-- {conf}")
        c = find_pattern_in_service_config(serviceconfig, conf)
        if c is not None:
            print("\tFound in service config")
            overrideconfig.append(c)
            continue
        else:
            for val in vals:
                stop_service(service_name)
                print("\tservice stopped")
                buffer = "\n".join(overrideconfig)
                buffer += f"\n{conf}={val}"
                print(f"\t{conf}={val}")    
                # Writing to a text file
                with open(f"/run/systemd/system/{service_name}.d/override.conf", 'w') as file:
                    file.write(buffer)
                reload_systemd()
                print(f"\t\tDaemon reloaded")
                time.sleep(8)
                start_service(service_name)
                print("\t\tService started")
                time.sleep(6)
                if is_service_active(service_name):
                    stop_service(service_name)
                    overrideconfig.append(f"{conf}={val}")
                    print(f"\t\t======>Config Final {conf}={val}") 
                    out = sh.sudo("rm", "-rf", f"/run/systemd/system/{service_name}.d/")
                    out = sh.sudo("mkdir", f"/run/systemd/system/{service_name}.d/")
                    reload_systemd()
                    print(f"\t\tDaemon reloaded")
                    time.sleep(4)
                    start_service(service_name)
                    time.sleep(2)
                    print("Srevice Active?", is_service_active(service_name))
                    break
                else:
                    out = sh.sudo("rm", "-rf", f"/run/systemd/system/{service_name}.d/")
                    #start_service(service_name)
                    #if is_service_active(service_name) == False:
                    #    print("Unable to restore service!")
                    #    exit()
                    out = sh.sudo("mkdir", f"/run/systemd/system/{service_name}.d/")
                    time.sleep(2)
                    reload_systemd()
                    print(f"\t\tDaemon reloaded")
                    time.sleep(4)
                    start_service(service_name)
                    time.sleep(2)
                    print("Srevice Active?", is_service_active(service_name))

                #overrideconfig.append()

        '''
        if check_service_status(SERVICE_NAME):
            print(f"{SERVICE_NAME} is running.")
            break  # Exit the loop if the service is running
        else:
            print(f"{SERVICE_NAME} is not running. Attempting to start...")
            start_service(SERVICE_NAME)

            # Check the status again
            time.sleep(2)  # Give it a moment to start
            if not check_service_status(SERVICE_NAME):
                print(f"{SERVICE_NAME} failed to start. Performing custom task...")
                custom_task()
                print(f"Reloading systemd daemon for {SERVICE_NAME}...")
                reload_systemd()
        '''
if __name__ == "__main__":
    main()
