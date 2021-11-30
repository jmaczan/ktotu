import json
from os import path
from mappers import *
from constants import user_files_directory_path

prefix = path.expanduser('~')+'/'+user_files_directory_path+'/'

devices_filename = 'devices.json'
network_filename = 'network.json'

def read_json_from_file(filename):
    try:
        with open(prefix+filename) as file:
            raw_json = file.read()
            return json.loads(raw_json)
    except IOError:
        raise IOError

def write_json_to_file(payload, filename):
    with open(prefix+filename, 'w') as file:
        file.write(json.dumps(payload))

def read_known_devices_from_file():
    try:
        known_devices = read_json_from_file(devices_filename)
        known_mac_addresses = devices_to_mac_addresses(known_devices)
        return (known_devices, known_mac_addresses)
    except IOError:
        known_devices = {}
        known_mac_addresses = []
        return (known_devices, known_mac_addresses)

def write_known_devices_to_file(known_devices):
    write_json_to_file(known_devices, devices_filename)

def read_network_from_file():
    try:
        return read_json_from_file(network_filename)
    except IOError:
        return {}

def write_network_to_file(network):
    write_json_to_file(network, network_filename)
