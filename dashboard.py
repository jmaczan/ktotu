from files_io import read_known_devices_from_file, read_network_from_file
from mappers import count_unmapped_devices

def dashboard():
    (known_devices, _) = read_known_devices_from_file()
    unmapped_devices_number = count_unmapped_devices(known_devices)
    network = read_network_from_file()

    print("Dashboard:\n")
    print("You know %s devices:\n  * %s devices are tagged\n  * %s devices are not tagged\n" % (len(known_devices), len(known_devices)-unmapped_devices_number, unmapped_devices_number))
    if 'ip_range' in network and 'interface' in network:
        print("Network that you monitor:\n  * IP range: %s\n  * Interface: %s" % (network['ip_range'], network['interface']))
    else:
        print("You didn't configure network yet. You can do it using command 'network'")
    print("\nType 'commands' or 'help' for assistance.")
    print("Press Ctrl+C or type 'quit' or 'q' to quit")
    print("At any time press Enter to return to dashboard.")