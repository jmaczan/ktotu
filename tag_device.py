from mappers import *
from files_io import *
from scan import *

def tag_device():
    print("Tag device:\n")
    
    (known_devices, _) = read_known_devices_from_file()
    
    print("I'm scanning your network now... It will take about 25 seconds. Future versions will be faster, I promise.")
    
    scanned_mac_addresses = scan_for_mac_addresses()
    scanned_devices = mac_addresses_to_dict(scanned_mac_addresses)
    
    if len(known_devices) == 0:
        known_devices = scanned_devices
    print("\nDone. \n")
    
    devices_mapping_result_infos = {}
    
    print("Please disconnect only one device from your network. It might be smartphone, laptop, pc, smart tv, tablet, router, tv box and so on. Please do it now.")
    
    device_name = input("\nOnce you disconnect this device, please provide its name.\n\nDevice name: ")
        
    print("\nOkay. I'm scanning your network again to discover which device disappeared, by comparing list of connected devices...")
    print("\nIt will take a while as well...")
    
    rescanned_mac_addresses = scan_for_mac_addresses()
    
    print("\nDone.\n")
    
    devices_missing_after_scan = list(filter(lambda device: device not in rescanned_mac_addresses, scanned_mac_addresses))
    print("Disconnected devices: %s" % (", ".join(devices_missing_after_scan) if len(devices_missing_after_scan) > 0 else "none"))
    new_devices_after_scan = list(filter(lambda device: device not in scanned_mac_addresses, rescanned_mac_addresses))
    print("Unknown devices found: %s" % (", ".join(new_devices_after_scan) if len(new_devices_after_scan) > 0 else "none"))
    
    if len(devices_missing_after_scan) > 0:
        if len(devices_missing_after_scan) > 1:
            devices_mapping_result_infos['more_than_single_missing'] = "There is more than one device disconnected. Maybe your device holds more that one MAC address or maybe some device disconnected in a meantime. Please investigate it. You can experiment with running 'listen' and connecting and disconnecting device in order to be sure that you tagged device correctly."
        for i in range(0, len(devices_missing_after_scan)):
            if devices_missing_after_scan[i] in list(known_devices.keys()) and known_devices[devices_missing_after_scan[i]]['name'] != '':
                devices_mapping_result_infos['already_mapped_device_missing'] = "During the mapping, some your device that is already mapped gone disconnected. I didn't change this devices name or saved MAC Address. Performing mapping check is strongly recommended."
            else:
                if devices_missing_after_scan[i] not in list(known_devices.keys()):
                    known_devices[devices_missing_after_scan[i]] = {'name': device_name}
                else:
                    known_devices[devices_missing_after_scan[i]]['name'] = device_name
    
    for i in range(0, len(new_devices_after_scan)):
        known_devices[new_devices_after_scan[i]] = {'name': ''}
    
    write_known_devices_to_file(known_devices)
    
    if len(devices_missing_after_scan) == 0:
        print("\nI didn't tag any device, because I didn't notice any change in connected devices when you disconnected the device.")
        print("Maybe you didn't disconnect the device or it wasn't connected to this network.")
    elif len(devices_missing_after_scan) == 1:
        print("\nI successfully tagged device as %s (MAC address - %s)" % (device_name, devices_missing_after_scan[0]))

    devices_mapping_result_infos_list = list(devices_mapping_result_infos.values())
    if len(devices_mapping_result_infos_list) > 0:
        print("")
        for i in range(0, len(devices_mapping_result_infos_list)):
            print(devices_mapping_result_infos_list[i])
        print("")
