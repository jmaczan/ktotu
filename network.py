from files_io import write_network_to_file

def configure_network():
    print("Configure network:\n")
    print("To use ktotu you need to decide which network you want to scan.")
    print("\nPlease provide IP range and interface.")
    print("\nSample IP range: 192.168.0.0/24")
    print("Sample interface: wlp1s0")
    raw_ip_range = input("\nIP range: ")
    ip_range = raw_ip_range.strip()
    raw_interface = input("Interface: ")
    interface = raw_interface.strip()
    write_network_to_file({'ip_range': ip_range, 'interface': interface})
    print("Done")
