import subprocess
import time

SERVICE_NAME = 'your_service_name'  # Replace with your service name

def check_service_status(service_name):
    try:
        result = subprocess.run(
            ['systemctl', 'is-active', service_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return result.stdout.strip() == 'active'
    except subprocess.CalledProcessError:
        return False

def start_service(service_name):
    subprocess.run(['systemctl', 'start', service_name], check=True)

def reload_systemd():
    subprocess.run(['systemctl', 'daemon-reload'], check=True)

def custom_task():
    # Add your custom task here
    print("Performing custom task...")

def main():
    while True:
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

if __name__ == "__main__":
    main()

