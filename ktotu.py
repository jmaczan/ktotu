from keyboard_interrupt import handle_keyboard_interrupt
from menu import *
from prevent_root import prevent_root

def ktotu():
    prevent_root()
    menu()

handle_keyboard_interrupt(ktotu)