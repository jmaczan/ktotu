from typing import List, Text


def parse_cli_command_arguments(arguments: List):
    return (arguments[1], arguments[2:])

def parse_text_command_arguments(arguments: Text):
    commands_and_arguments = arguments.split(' ')
    return (commands_and_arguments[0], commands_and_arguments[1:])