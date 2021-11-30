from files_io import read_known_devices_from_file
from typing import Dict

def print_known_devices(known_devices = None):
    if known_devices == None:
        (known_devices, _) = read_known_devices_from_file()
    for index, device in enumerate(known_devices):
        print("[%s] %s - %s" % (index, (""+known_devices[device]['name'] if known_devices[device]['name'] != '' else "Untagged device"), device))
def print_known_mac_addresses(known_mac_addresses = None):
    if known_mac_addresses == None:
        (_, known_mac_addresses) = read_known_devices_from_file()
    print("\n".join(known_mac_addresses))