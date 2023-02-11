""" Util containing validator used for Advent of Code run initialization
Author: Ic4r0 - https://github.com/Ic4r0
Created: 11th February 2023
"""


def check_valid_arguments(arguments_list: list[str]) -> (int, int):
    """ Check if the inserted arguments are valid
    :param arguments_list: list of arguments
    :return: tuple containing selected day and selected part
    """
    if len(arguments_list) > 0:
        if len(arguments_list) == 2 and arguments_list[0].isnumeric() and arguments_list[1].isnumeric():
            return int(arguments_list[0]), int(arguments_list[1])
        elif len(arguments_list) == 1 and arguments_list[0].isnumeric():
            return int(arguments_list[0]), None
        else:
            return None
    else:
        return None
