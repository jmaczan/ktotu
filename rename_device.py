from files_io import read_known_devices_from_file, write_known_devices_to_file
from pretty_print import print_known_devices

def rename_device(arguments):
    print("Rename device:\n")
    print("[id] Tag - MAC address\n")
    if(arguments == None or len(arguments) == 0):
        (id, name) = get_id_and_name_from_user()
        rename_device_by_id_and_name(id, name)
        return

    (id, name) = get_id_and_name_from_arguments(arguments)
    
    if(id == None or name == None):
        return

    rename_device_by_id_and_name(id, name)

def rename_device_by_id_and_name(id, name):
    (known_devices, _) = read_known_devices_from_file()

    if(id >= len(known_devices)):
        print("\nThere is no device with id %s. You can choose devices from range 0 - %s" % (id, len(known_devices)-1))
        return

    known_devices[list(known_devices.keys())[id]]['name'] = name
    write_known_devices_to_file(known_devices)
    print("Done")

def get_id_and_name_from_user():
    print_known_devices()
    print("\nEach device has it's unique id, listed as first value in square brackets, i.e. [2].")
    print("\nPlease provide the id and new name for this devices.")
    print("Example: 2 my new laptop")
    raw_id = input("\nProvide id: ")
    id = int(raw_id.strip())
    raw_name = input("\nProvide new name: ")
    name = raw_name.strip()
    print("")
    return (id, name)

def get_id_and_name_from_arguments(arguments):
    if(len(arguments) < 2):
        print("Invalid argument. It should be a number followed by new name of device")
        print("Example: ktotu r 2 my new shiny laptop")
        return (None, None)

    return (int(arguments[0].strip()), " ".join(arguments[1:]))