""" Day 4: High-Entropy Passphrases
Author: Ic4r0 - https://github.com/Ic4r0
Created: 1st December 2023
"""

# imports
from utils.parse_input import parse_by_line


# modules
def part_1(input_list: list) -> int:
    """ Code for the 1st part of the 4th day of Advent of Code
    :param input_list: input list
    :return: numeric result
    """
    valid_passphrases = 0
    for passphrase in input_list:
        duplicate_count = {}
        for part in passphrase.split(' '):
            if part not in duplicate_count:
                duplicate_count[part] = 0
            duplicate_count[part] += 1
        if all(value == 1 for value in duplicate_count.values()):
            valid_passphrases += 1
    return valid_passphrases


def part_2(input_list: list) -> int:
    """ Code for the 1st part of the 4th day of Advent of Code
    :param input_list: input list
    :return: numeric result
    """
    valid_passphrases = 0
    for passphrase in input_list:
        splitted_passphrase = passphrase.split(' ')
        parts_by_length = {}
        current_part_length = 1
        while len(splitted_passphrase) > 0:
            curr_len_list = [
                idx if len(val) == current_part_length else -1 for idx, val in enumerate(splitted_passphrase)
            ]
            curr_len_filter = list(filter(lambda x: (x >= 0), curr_len_list))
            curr_len_filter.reverse()
            for part_idx in curr_len_filter:
                if current_part_length not in parts_by_length:
                    parts_by_length[current_part_length] = []
                parts_by_length[current_part_length].append(splitted_passphrase.pop(part_idx))
            current_part_length += 1
        parts_by_length_values = parts_by_length.values()
        for idx, parts in enumerate(parts_by_length_values):
            reordered_parts = [''.join(sorted(part)) for part in parts]
            reordered_parts_no_duplicates = list(dict.fromkeys(reordered_parts))
            if len(reordered_parts) == len(reordered_parts_no_duplicates) and idx == len(parts_by_length_values) - 1:
                valid_passphrases += 1
            elif len(reordered_parts) == len(reordered_parts_no_duplicates):
                continue
            else:
                break
    return valid_passphrases


def day_4(selected_part: int = None, test: bool = False) -> (int, int):
    """ Needed to select which part of the 4th day we want to execute
    :param selected_part: selected Advent of Code part of the 4th day
    :param test: flag to use test input
    """
    passphrase_list = parse_by_line(4, int_list=False, is_test=test)
    result_part_1 = 0
    result_part_2 = 0
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(passphrase_list)
        print('The result of 1st part of the 4th day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(passphrase_list)
        print('The result of 2nd part of the 4th day of AoC is: ' + str(result_part_2))
    return result_part_1, result_part_2
