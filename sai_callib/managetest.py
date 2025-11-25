import os
import sys
import subprocess

# def map_network_drive():
#     # Full path to net.exe
#     net_path = r'C:\Windows\System32\net.exe'

#     # Step 1: Disconnect all existing connections to any network drives
#     print("Disconnecting all existing network connections...")
#     disconnect_cmd = f'cmd /c "{net_path} use * /delete /yes"'
#     subprocess.run(disconnect_cmd, shell=True)

#     # Step 2: Delete Z: mapping if exists
#     print("Deleting existing Z: mapping (if any)...")
#     del_cmd = f'cmd /c "{net_path} use Z: /delete /yes"'
#     subprocess.run(del_cmd, shell=True)

#     # Step 3: Map new Z: drive
#     print("Mapping Z: drive to \\\\raspberrypi\\four_channel_db ...")
#     map_cmd = f'cmd /c "{net_path} use Z: \\\\raspberrypi\\four_channel_db /user:sai sai@123 /persistent:yes"'
#     result = subprocess.run(map_cmd, shell=True)

#     if result.returncode != 0:
#         print("❌ Error: Failed to map Z: drive. Please check credentials or network path.")
#         sys.exit(1)
#     else:
#         print("✅ Z: drive mapped successfully.")

def main():
    # map_network_drive()
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sai_calibrations.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Make sure it's installed and your virtual environment is active."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
