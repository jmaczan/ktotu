from clear_terminal import clear_terminal
from pretty_print import print_known_devices
from mappers import mac_addresses_to_dict
from scan import scan_for_mac_addresses
from files_io import read_known_devices_from_file, write_known_devices_to_file
from subprocess import PIPE, run
import time
import sys

def listen(arguments = None):
    listening_interval = get_listening_interval_from_arguments(arguments) or 0

    print("Listen:\n")
    all_unknown_mac_addresses = []
    (known_devices, known_mac_addresses) = read_known_devices_from_file()
    while(1):
        print("Scanning...")
        all_unknown_mac_addresses = listen_step(all_unknown_mac_addresses, known_devices, known_mac_addresses)
        if (len(all_unknown_mac_addresses) > 0):
            print("\nUnknown devices found during listening:")
            print("\n".join(all_unknown_mac_addresses))

        print()
        sleep_before_listen_step(listening_interval)

def listen_step(all_unknown_mac_addresses, known_devices, known_mac_addresses):
    scanned_mac_addresses = scan_for_mac_addresses()
    scanned_devices = mac_addresses_to_dict(scanned_mac_addresses)
    clear_terminal()
    print("Listen:\n")
    print("Connected devices:")
    print_known_devices(scanned_devices)
    unknown_mac_addresses = list(filter(lambda device: device not in known_mac_addresses and device not in all_unknown_mac_addresses, scanned_mac_addresses))
    if (len(unknown_mac_addresses) > 0):
        print("\nNew unknown device%s!" % ("s" if len(unknown_mac_addresses) > 1 else ""))
        print("%s" % ("\n".join(unknown_mac_addresses)))
        unknown_scanned_devices = mac_addresses_to_dict(unknown_mac_addresses)
        write_known_devices_to_file({**known_devices, **unknown_scanned_devices})
        print("\nI saved %s for you." % ("them" if len(unknown_mac_addresses) > 1 else "it"))
    return all_unknown_mac_addresses + unknown_mac_addresses

def sleep_before_listen_step(seconds_left):
    if(seconds_left <= 0):
        return
    sys.stdout.write("\r" + "Next scan in %s..." % seconds_left)
    time.sleep(1)
    sys.stdout.flush()
    sleep_before_listen_step(seconds_left-1)

def get_listening_interval_from_arguments(arguments):
    if(arguments == None or len(arguments) == 0):
        return None
    
    if(len(arguments) > 1):
        print("You can pass only a single number value as parameter. It should be number of seconds between scans.")
        return None
    
    return int(arguments[0].strip())