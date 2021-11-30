from pretty_print import print_known_devices


def devices():
    print("Tagged and untagged devices:\n")
    print("[id] Tag - MAC address\n")
    print_known_devices()