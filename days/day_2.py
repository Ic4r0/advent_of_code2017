""" Day 2: Corruption Checksum
Author: Ic4r0 - https://github.com/Ic4r0
Created: 29th November 2023
"""

# imports
from utils.parse_input import parse_by_line
from re import match


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 2nd day of Advent of Code
    :param input_list: input list
    :return: numeric result
    """
    difference_list = [max(sublist) - min(sublist) for sublist in input_list]
    return sum(difference_list)


def part_2(input_list: list) -> int:
    """ Code for the 2nd part of the 2nd day of Advent of Code
    :param input_list: input list
    :return: numeric result
    """
    values_to_be_summed = []
    for row in input_list:
        for idx, number in enumerate(row):
            modulo_list = [row[i] if number % row[i] == 0 and i != idx else 0 for i in range(len(row))]
            if sum(modulo_list) > 0:
                values_to_be_summed.append(number / sum(modulo_list))
                break
    return int(sum(values_to_be_summed))


def day_2(selected_part: int = None, test: bool = False) -> (int, int):
    """ Needed to select which part of the 2nd day we want to execute
    :param selected_part: selected Advent of Code part of the 2nd day
    :param test: flag to use test input
    """
    input_list = parse_by_line(2, int_list=False, is_test=test)
    values_lines = []
    for row in input_list:
        split_row = row.split(' ')
        if len(split_row) == 1:
            split_row = row.split('\t')
        values = [int(gr) for gr in split_row]
        values_lines.append(values)
    result_part_1 = 0
    result_part_2 = 0
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(values_lines)
        print('The result of 1st part of the 2nd day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(values_lines)
        print('The result of 2nd part of the 2nd day of AoC is: ' + str(result_part_2))
    return result_part_1, result_part_2
