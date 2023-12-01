""" Day 5: A Maze of Twisty Trampolines, All Alike
Author: Ic4r0 - https://github.com/Ic4r0
Created: 1st December 2023
"""

# imports
from utils.parse_input import parse_by_line


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 5th day of Advent of Code
    :param input_list: input list
    :return: numeric result
    """
    steps = 0
    current_idx = 0
    while 0 <= current_idx < len(input_list):
        previous_idx = current_idx
        current_value = input_list[previous_idx]
        current_idx += current_value
        input_list[previous_idx] += 1
        steps += 1
    return steps


def part_2(input_list: list) -> int:
    """ Code for the 1st part of the 5th day of Advent of Code
    :param input_list: input list
    :return: numeric result
    """
    steps = 0
    current_idx = 0
    while 0 <= current_idx < len(input_list):
        previous_idx = current_idx
        current_value = input_list[previous_idx]
        current_idx += current_value
        if current_value >= 3:
            input_list[previous_idx] -= 1
        else:
            input_list[previous_idx] += 1
        steps += 1
    return steps


def day_5(selected_part: int = None, test: bool = False) -> (int, int):
    """ Needed to select which part of the 5th day we want to execute
    :param selected_part: selected Advent of Code part of the 5th day
    :param test: flag to use test input
    """
    jump_offsets = parse_by_line(5, is_test=test)
    result_part_1 = 0
    result_part_2 = 0
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(jump_offsets[:])
        print('The result of 1st part of the 5th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(jump_offsets[:])
        print('The result of 2nd part of the 5th day of AoC is: ' + str(result_part_2))
    return result_part_1, result_part_2
