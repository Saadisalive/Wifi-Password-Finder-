import subprocess

def get_wifi_password(ssid):
    try:
        # Run the command to get the Wi-Fi profile details
        command = f'netsh wlan show profile name="{ssid}" key=clear'
        result = subprocess.run(command, capture_output=True, text=True, shell=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            output = result.stdout
            # Search for the "Key Content" line which contains the password
            for line in output.splitlines():
                if "Key Content" in line:
                    password = line.split(":")[1].strip()
                    return password
            return "Password not found in the profile."
        else:
            return "Error: Unable to retrieve Wi-Fi profile."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
ssid = input("Put Your SSID: ")
password = get_wifi_password(ssid)
print(f"The password for Wi-Fi '{ssid}' is: {password}")