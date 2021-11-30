from sys import exit

from clear_terminal import clear_terminal

def handle_keyboard_interrupt(function_to_wrap):
    try:
        function_to_wrap()
    except KeyboardInterrupt:
        clear_terminal()
        print("Bye")
        exit()