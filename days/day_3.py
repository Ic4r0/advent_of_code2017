""" Day 3: Spiral Memory
Author: Ic4r0 - https://github.com/Ic4r0
Created: 29th November 2023
"""

# imports
from utils.parse_input import parse_single_line


# modules
def spiral_stress_sum(current_coordinate: tuple, passed_coordinates: dict) -> int:
    """ Method to compute the current value for the 2nd part
    :param current_coordinate: (x, y) tuple
    :param passed_coordinates: {(x, y): value, ...}
    :return: numeric result
    """
    x, y = current_coordinate
    sum_value = (passed_coordinates.get((x - 1, y + 1), 0) + passed_coordinates.get((x, y + 1), 0) +
                 passed_coordinates.get((x + 1, y + 1), 0) + passed_coordinates.get((x - 1, y), 0) +
                 passed_coordinates.get((x + 1, y), 0) + passed_coordinates.get((x - 1, y - 1), 0) +
                 passed_coordinates.get((x, y - 1), 0) + passed_coordinates.get((x + 1, y - 1), 0))
    passed_coordinates[current_coordinate] = sum_value
    return sum_value


def part_1(input_number: int) -> int:
    """ Code for the 1st part of the 3rd day of Advent of Code
    :param input_number: input number
    :return: numeric result
    """
    current_odd = 1
    while current_odd ** 2 < input_number:
        current_odd += 2
    h_steps = int((current_odd - 3) / 2 + 1)
    current_odd -= 2
    # create tuple (x, y) where 1 is at coordinates (0, 0)
    # starting coordinate at
    current_coordinate = (h_steps, -h_steps + 1)
    # starting value at
    current_value = current_odd ** 2 + 1
    # max number of steps in one direction equal to current odd + 1
    current_step = 1
    for direction in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
        while current_step < current_odd + 1 and current_value != input_number:
            current_coordinate = tuple(map(sum, zip(current_coordinate, direction)))
            current_value += 1
            current_step += 1
        if current_value == input_number:
            break
        current_step = 0
    x, y = current_coordinate
    return abs(x) + abs(y)


def part_2(input_number: int) -> int:
    """ Code for the 1st part of the 3rd day of Advent of Code
    :param input_number: input number
    :return: numeric result
    """
    passed_coordinates = {(0, 0): 1, (1, 0): 1, (1, 1): 2, (0, 1): 4, (-1, 1): 5, (-1, 0): 10, (-1, -1): 11,
                          (0, -1): 23, (1, -1): 25, (2, -1): 26}
    current_odd = 3
    # create tuple (x, y) where 1 is at coordinates (0, 0)
    # starting coordinate at
    current_coordinate = (2, -1)
    # starting value at
    current_value = 26
    # max number of steps in one direction equal to current odd + 1
    current_step = 1
    while current_value < input_number:
        for direction in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
            while current_step < current_odd + 1 and current_value < input_number:
                current_coordinate = tuple(map(sum, zip(current_coordinate, direction)))
                current_value = spiral_stress_sum(current_coordinate, passed_coordinates)
                current_step += 1
            if current_value >= input_number:
                break
            current_step = 0
        if current_value >= input_number:
            break
        current_odd += 2
        current_step = 1
        current_coordinate = tuple(map(sum, zip(current_coordinate, direction)))
        current_value = spiral_stress_sum(current_coordinate, passed_coordinates)
    return current_value


def day_3(selected_part: int = None, test: bool = False) -> (int, int):
    """ Needed to select which part of the 3rd day we want to execute
    :param selected_part: selected Advent of Code part of the 3rd day
    :param test: flag to use test input
    """
    puzzle_input = int(parse_single_line(3, is_test=test).strip())
    result_part_1 = 0
    result_part_2 = 0
    if selected_part == 1 or not selected_part:
        result_part_1 = part_1(puzzle_input)
        print('The result of 1st part of the 3rd day of AoC is: ' + str(result_part_1))
    if selected_part == 2 or not selected_part:
        result_part_2 = part_2(puzzle_input)
        print('The result of 2nd part of the 3rd day of AoC is: ' + str(result_part_2))
    return result_part_1, result_part_2
