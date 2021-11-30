def count_unmapped_devices(devices):
    counter = 0
    for device in list(devices.values()):
        if device['name'] == '':
            counter+=1
    return counter

def devices_to_mac_addresses(devices):
    return list(devices.keys())

def mac_addresses_to_dict(mac_addresses):
    return { mac_addresses[i]: {'name': '' } for i in range(0, len(mac_addresses)) }

def mac_addresses_to_devices(mac_addresses, devices):
    return { devices[mac_addresses[i]]: {'name': '' } for i in range(0, len(mac_addresses)) }
