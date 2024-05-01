#!/usr/bin/env/python

import random
import os

red = "\033[91m"  # Define red color code
lblue = "\033[94m"  # Define light blue color code
grn = "\033[32m"
reset = "\033[0m"  # Define reset color code

mac_list = [
    "00:69:A6:7A:67:31",
    "00:27:AE:10:A7:9F",
    "00:F2:CB:B4:70:77",
    "00:C6:F7:1D:F2:72",
    "00:04:C2:C0:B0:A9",
    "00:69:A6:7A:67:31",
    "00:27:AE:10:A7:9F",
    "00:F2:CB:B4:70:77",
    "00:C6:F7:1D:F2:72",
    "00:04:C2:C0:B0:A9",
    "77:69:A6:7A:67:31",
    "17:27:AE:10:A7:9F",
    "11:F2:CB:B4:70:77",
    "00:C6:F7:1D:F2:72",
    "F3:04:C2:C0:B0:A9",
    "93:FD:3A:A3:7A:CF",
    "C6:17:50:DC:6C:92",
    "25:C6:9B:0C:5D:5A",
    "00:6A:B3:0C:66:67",
    "91:8E:98:FC:B5:B6",
    "6C:1B:55:E7:5D:79",
    "11:BE:57:8D:7A:E7",
    "ED:8D:74:F8:5B:1F",
    "7F:8A:C1:1A:24:81",
    "54:DB:79:51:14:E2",
    "F2:3E:DB:34:0D:A0",
    "F2:6A:F0:5F:C4:E1",
    "45:61:4A:B1:3C:93",
    "82:65:D1:81:26:C3",
    "A5:C1:16:71:91:89",
    "4E:D0:AE:EA:65:B6",
    "5E:F5:CD:79:3D:CB",
    "0D:A7:D0:46:11:4C",
    "39:20:55:8C:CF:40",
    "B3:0B:BB:06:9F:A2",
    "77:FD:71:E2:E1:4D",
    "9E:7D:56:2C:E0:17",
    "CE:59:4C:F2:40:2E",
    "D2:08:8A:44:C4:07",
    "98:A1:D8:E0:EF:D2",
    "81:ED:D0:28:1A:93",
    "12:78:29:97:B3:21",
    "FE:DC:30:3B:08:44",
    "DB:91:AB:75:A3:F8",
    "30:B4:7D:1E:B8:FE",
    "E7:1D:F6:2B:E2:B2",
    "AA:7C:A8:43:CC:DF",
    "31:F0:A1:66:BD:3A",
    "AE:EA:1D:B3:7E:3E",
    "F1:52:0C:1A:C7:45",
    "98:33:C7:95:E5:C7",
    "26:CB:7A:27:7F:ED",
    "4E:A5:7A:DB:35:D4",
    "98:7A:3A:0B:0A:D2",
    "B1:39:5A:D3:6B:FB",
    "F1:73:E2:C9:8F:2A",
    "4B:CA:6D:F7:81:CD",
    "83:5D:F0:4B:53:C7",
    "7E:3F:FB:77:2C:D0",
    "98:AE:51:6E:3A:07",
    "AA:E0:5B:42:C3:29",
    "F8:E9:11:0D:2E:27",
    "E5:2D:3A:B7:D6:2D"
    "00:2D:3A:B7:D6:2D"
    # ... (more valid MAC addresses can be added here)
]


def is_valid_mac(mac_address):
    """
    Checks if the given string is a valid MAC address.

    Args:
        mac_address: The string to be validated.

    Returns:
        True if the string is a valid MAC address, False otherwise.
    """

    # Check length (17 characters)
    if len(mac_address) != 17:
        return False

    # Check format (XX:XX:XX:XX:XX:XX)
    if not all(c.isalnum() and len(c) == 2 for c in mac_address.split(':')):
        return False

    return True


print(f"{red}MAC Changer{reset}")
print(f"{lblue}1. Random MAC{reset}")
print(f"{lblue}2. Custom MAC{reset}")
print(f"{lblue}3. Exit{reset}")


choice = input(f"{red}Enter your choice (1-3):{reset}")

if choice == '1':
    new_mac = random.choice(mac_list)
    print(f"New MAC address: {new_mac}")
    confirmation = input(f"Confirm change? ({grn}y{reset}/{red}n{reset}): ").lower()
    if confirmation == 'y':
        interface = input("Enter network interface (e.g., eth0, wlan0): ")
        try:
            os.system("ifconfig " + interface + " down")
            os.system("ifconfig " + interface + " hw ether " + new_mac)
            os.system("ifconfig " + interface + " up")
            print(f"{grn}Successfully changed MAC address of {interface} to {new_mac}{grn}")
        except Exception as e:
            print(f"{red}Error: Failed to change MAC address. Reason: {e}{reset}")

elif choice == '2':
    while True:
        custom_mac = input("Enter a custom MAC address (XX:XX:XX:XX:XX:XX): ")
        if is_valid_mac(custom_mac):
            new_mac = custom_mac.upper()  # Ensure uppercase for consistency
            break
        else:
            print(f"{red}Invalid MAC address format. Please try again.{reset}")

    print(f"New MAC address: {new_mac}")
    confirmation = input(f"Confirm change? ({grn}y{reset}/{red}n{reset}): ").lower()

    if confirmation == 'y':
        interface = input("Enter network interface (e.g., eth0, wlan0): ")
        try:
            os.system("ifconfig " + interface + " down")
            os.system("ifconfig " + interface + " hw ether " + new_mac)
            os.system("ifconfig " + interface + " up")
            print(f"{grn}Successfully changed MAC address of {interface} to {new_mac}{grn}")
        except Exception as e:
            print(f"{red}Error: Failed to change MAC address. Reason: {e}{reset}")

elif choice == '3':
    pass  # Exit

print(reset)  # Reset terminal color to default (optional)
