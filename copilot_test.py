import os
import platform
import subprocess

def print_system_uptime():
    system = platform.system()
    if system == "Windows":
        # Windows: Use 'net stats srv' and parse output for uptime
        try:
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    print(f"System uptime (Windows): {line}")
                    return
            print("Could not determine uptime on Windows.")
        except Exception as e:
            print(f"Error getting uptime on Windows: {e}")
    elif system in ["Linux", "Darwin"]:
        # Linux/Mac: Use 'uptime' command
        try:
            output = subprocess.check_output(["uptime"], text=True)
            print(f"System uptime ({system}): {output.strip()}")
        except Exception as e:
            print(f"Error getting uptime on {system}: {e}")
    else:
        print(f"Unsupported OS: {system}")

if __name__ == "__main__":
    print_system_uptime()
