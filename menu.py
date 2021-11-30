from about import about
from clear_terminal import clear_terminal
from commands import commands
from dashboard import dashboard
from devices import devices
from navigation import navigation
from listen import listen
from macs import macs
from network import configure_network
from parsers import parse_cli_command_arguments, parse_text_command_arguments
from forget_device import forget_device
from quit import quit_ktotu
from rename_device import rename_device
from files_io import *
from tag_device import *
from pretty_print import *
from help import *
from scan import *
from sys import argv

def menu():
    clear_terminal()
    print("Hello in ktotu\n")

    if len(argv) > 1:
        single_command_execution(argv)
    else:
        interactive_menu()

def single_command_execution(arguments):
    (command, arguments) = parse_cli_command_arguments(arguments)
    run_command(command, arguments)

def interactive_menu():
    dashboard()
    navigation()

    while(1):
        raw_command_and_arguments = input("\nktotu: ")
        clear_terminal()
        (command, arguments) = parse_text_command_arguments(raw_command_and_arguments)
        run_command(command, arguments)
    
def run_command(command, arguments = None):
    command = command.strip()
    
    if command == "quit" or command == "q":
        quit_ktotu()

    if command == "scan" or command == "s":
        scan()
    elif command == "listen" or command == "l":
        listen(arguments)
    elif command == "tag" or command == "t":
        tag_device()
    elif command == "devices" or command == "d":
        devices()
    elif command == "macs" or command == "m":
        macs()
    elif command == "network" or command == "n":
        configure_network()
    elif command == "rename" or command == "r":
        rename_device(arguments)
    elif command == "forget" or command == "f":
        forget_device(arguments)
    elif command == "commands" or command == "c":
        commands()
    elif command == "help" or command == "h":
        print_help()
    elif command == "about" or command == "a":
        about()
    elif command == "" or command == "dashboard":
        dashboard()
    else:
        print("Command %s not found. Type help for available commands" % command)
    navigation()
    