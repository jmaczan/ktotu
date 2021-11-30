from scapy.all import ARP, Ether, srp
from sys import exit, argv

def scanner(interface, ips_range):
    mac_addresses = []
    for _, results in srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ips_range), timeout=6, verbose=0, iface = interface, inter = 0.2)[0]:
        mac_addresses.append(results.hwsrc)
    return mac_addresses

if(len(argv) != 3):
    print("Incorrect params. Please provide interface and IPs range. Example: mac-addresses-scanner wlp1s0 192.168.0.0/24")
    exit()

print(scanner(argv[1], argv[2]))
