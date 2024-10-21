import subprocess
import os

def read_service_override_runtime(service_name: str):
    # Define the path to the runtime override configuration file
    override_dir = f"/run/systemd/system/{service_name}.d"
    override_file_path = os.path.join(override_dir, "override.conf")
    
    # Step 1: Run the `systemctl edit --runtime` to ensure the override file is created
    try:
        # Use subprocess to run systemctl edit --runtime non-interactively
        subprocess.run(['systemctl', 'edit', '--runtime', service_name], check=True)
        
        # Step 2: Read the existing content of the override.conf into a buffer
        if os.path.exists(override_file_path):
            with open(override_file_path, 'r') as override_file:
                override_content = override_file.read()
                print(f"Existing override content for {service_name}:\n{override_content}")
        else:
            print(f"No override file found for {service_name}.")
            override_content = ""
        
        return override_content

    except subprocess.CalledProcessError as e:
        print(f"Error running systemctl command: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Example usage
service_name = "bluetooth.service"  # Replace with the actual service name
override_content = read_service_override_runtime(service_name)

# Optionally modify the override_content and save it back if needed

