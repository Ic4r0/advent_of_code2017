""" Day 6: Memory Reallocation
Author: Ic4r0 - https://github.com/Ic4r0
Created: 1st December 2023
"""

# imports
from utils.parse_input import parse_single_line


# modules
def memory_reallocation(input_list: list) -> tuple:
    """ Code for the 1st part of the 6th day of Advent of Code
    :param input_list: input list
    :return: (steps, seen_configurations, new_config)
    """
    steps = 0
    memory_banks = len(input_list)
    seen_configurations = [''.join([str(val) for val in input_list])]
    while True:
        steps += 1
        blocks_value = max(input_list)
        max_idx = input_list.index(blocks_value)
        input_list[max_idx] = 0
        curr_idx = max_idx + 1
        while blocks_value > 0:
            if curr_idx == memory_banks:
                curr_idx = 0
            input_list[curr_idx] += 1
            blocks_value -= 1
            curr_idx += 1
        new_config = ''.join([str(val) for val in input_list])
        if new_config in seen_configurations:
            break
        seen_configurations.append(new_config)
    return steps, seen_configurations, new_config


def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 6th day of Advent of Code
    :param input_list: input list
    :return: numeric result
    """
    steps, _, _ = memory_reallocation(input_list)
    return steps


def part_2(input_list: list) -> int:
    """ Code for the 1st part of the 6th day of Advent of Code
    :param input_list: input list
    :return: numeric result
    """
    _, seen_configurations, new_config = memory_reallocation(input_list)
    first_occurrence = seen_configurations.index(new_config)
    return len(seen_configurations) - first_occurrence


def day_6(selected_part: int = None, test: bool = False) -> (int, int):
    """ Needed to select which part of the 6th day we want to execute
    :param selected_part: selected Advent of Code part of the 6th day
    :param test: flag to use test input
    """
    input_blocks = parse_single_line(6, is_test=test)
    splitted_input_blocks = [int(val) for val in input_blocks.split()]
    result_part_1 = 0
    result_part_2 = 0
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(splitted_input_blocks[:])
        print('The result of 1st part of the 6th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(splitted_input_blocks[:])
        print('The result of 2nd part of the 6th day of AoC is: ' + str(result_part_2))
    return result_part_1, result_part_2
