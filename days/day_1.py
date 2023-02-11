""" Day 1: Inverse Captcha
Author: Ic4r0 - https://github.com/Ic4r0
Created: 11th February 2023
"""

# imports
from utils.parse_input import parse_single_line


# modules
def part_1(input_str: str) -> int:
    """ Code for the 1st part of the 1st day of Advent of Code
    :param input_str: input string
    :return: numeric result
    """
    digits_sequence = input_str + input_str[0]
    captcha_sum = sum(int(first) for first, second in zip(digits_sequence, digits_sequence[1:]) if first == second)
    return captcha_sum


def part_2(input_str: str) -> int:
    """ Code for the 2nd part of the 1st day of Advent of Code
    :param input_str: input string
    :return: numeric result
    """
    input_length = len(input_str)
    input_for_zip = input_str[input_length//2:] + input_str
    captcha_sum = sum(int(first) for first, second in zip(input_str, input_for_zip) if first == second)
    return captcha_sum


def day_1(selected_part: int = None, test: bool = False) -> (int, int):
    """ Needed to select which part of the 1st day we want to execute
    :param selected_part: selected Advent of Code part of the 1st day
    :param test: flag to use test input
    """
    digits_sequence = parse_single_line(1, is_test=test).strip()
    result_part_1 = None
    result_part_2 = None
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(digits_sequence)
        print('The result of 1st part of the 1st day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(digits_sequence)
        print('The result of 2nd part of the 1st day of AoC is: ' + str(result_part_2))
    return result_part_1, result_part_2
