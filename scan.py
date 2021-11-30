from pretty_print import print_known_devices
from files_io import read_known_devices_from_file, read_network_from_file, write_known_devices_to_file
from mappers import mac_addresses_to_dict
from subprocess import PIPE, run, check_output
from os import system, path
from constants import mac_addresses_scanner, ktotu_path

def scan_for_mac_addresses():
    network = read_network_from_file()
    raw_mac_addresses = check_output(['sudo', ktotu_path+'/'+mac_addresses_scanner, network['interface'], network['ip_range']]).decode()
    trimmed_raw_mac_addresses = raw_mac_addresses[0:len(raw_mac_addresses)-1]
    return list(map(lambda mac_address: mac_address.strip('\''), trimmed_raw_mac_addresses.strip('][').split(', ')))

def scan():
    print("Scan:\n")
    (known_devices, known_mac_addresses) = read_known_devices_from_file()
    print("I'm scanning your network now... It will take about 25 seconds. Future versions will be faster, I promise")
    scanned_mac_addresses = scan_for_mac_addresses()
    scanned_devices = mac_addresses_to_dict(scanned_mac_addresses)
    
    if len(known_devices) == 0:
        print("You don't have any devices mapped in your network yet")
        print("I found these devices in your network now:")
        print_known_devices(scanned_devices)
        print("\nI save them for you. You can see list of them using 'd' or 'devices' command. In case you need mac addresses only, you can see them using 'm' or 'macs'.")
        write_known_devices_to_file(scanned_devices)
        return
    print("\nDone.\n")
    
    known_scanned_devices = list(map(lambda device: "%s - %s" % (known_devices[device]['name'] if known_devices[device]['name'] != '' else "Untagged device", device), filter(lambda device: device in known_mac_addresses, scanned_mac_addresses)))
    unknown_scanned_mac_addresses = list(filter(lambda device: device not in known_mac_addresses, scanned_mac_addresses))
    
    print("Scan result:\n")
    if len(unknown_scanned_mac_addresses) > 0:
        print("I discovered %s unknown device%s in your network!" % (len(unknown_scanned_mac_addresses), "s" if len(unknown_scanned_mac_addresses) > 1 else ""))
        print("MAC address%s: \n%s" % (("es" if len(unknown_scanned_mac_addresses) > 1 else ""), "\n".join(unknown_scanned_mac_addresses)))
        print("I saved %s for you.\n" % ("them" if len(unknown_scanned_mac_addresses) > 1 else "it"))
    else:
        print("I didn't find any unknown devices in your network.\n")
    print("Tagged and untagged that are online:\n\n%s" % ("\n".join(known_scanned_devices) if len(known_scanned_devices) > 0 else "none"))
    
    unknown_scanned_devices = mac_addresses_to_dict(unknown_scanned_mac_addresses)

    write_known_devices_to_file({**known_devices, **unknown_scanned_devices})
