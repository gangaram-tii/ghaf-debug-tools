import subprocess
import os

def read_service_override_runtime(service_name: str):
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
                print(f"Existing override content for {service_name}:\n{''.join(override_content)}")
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

def find_pattern_in_override_content(content, pattern):
    if content is not None:
        for line in content:
            if pattern in line:
                print(f"Found matching line: {line.strip()}")
                return line.strip()
        print(f"No matching line found for pattern '{pattern}'.")
    return None

# Example usage
service_name = "fail2ban.service"  # Replace with the actual service name
pattern = "ProtectHome"  # Replace with the pattern you want to search for

override_content = read_service_override_runtime(service_name)
matching_line = find_pattern_in_override_content(override_content, pattern)
