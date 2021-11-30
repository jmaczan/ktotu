from files_io import read_known_devices_from_file, write_known_devices_to_file
from pretty_print import print_known_devices

def forget_device(arguments):
    print("Forget device:\n")
    print("[id] Tag - MAC address\n")
    if(arguments == None or len(arguments) == 0):
        id = get_id_from_user()
        if(id == None):
            return
        forget_device_by_id(id)
        return
    
    id = get_id_from_arguments(arguments)
    
    if(id == None):
        return
    
    forget_device_by_id(id)

def forget_device_by_id(id):
    (known_devices, _) = read_known_devices_from_file()

    if(id >= len(known_devices)):
        print("There is no device with id %s." % (id), end="")
        if (len(known_devices) > 1):
            print(" You can choose devices from range 0 - %s" % (len(known_devices)-1), end="")
        print("")
        return

    mac_address = list(known_devices.keys())[id]
    name = list(known_devices.values())[id]['name']
    known_devices.pop(mac_address)
    write_known_devices_to_file(known_devices)
    print("Done. I forgot %s #%s with mac address %s" % ((name if name != '' else "unnamed device"), id, mac_address))

def get_id_from_user():
    print_known_devices()
    print("\nEach device has it's unique id, listed as first value in square brackets, i.e. [2].")
    print("\nPlease provide number of device that you want to forget.")
    print("Example: 12")
    raw_id = input("\nProvide id: ")
    print("")
    return to_int(raw_id.strip())

def get_id_from_arguments(arguments):
    if(len(arguments) != 1):
        print("Invalid argument. It should be a number.")
        print("Example: ktotu f 2")
        return
    
    return to_int(arguments[0].strip())

def to_int(text):
    try:
        result_int = int(text)
        return result_int
    except:
        print("Couldn't map given parameter to number value.")
        return None