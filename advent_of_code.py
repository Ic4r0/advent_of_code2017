""" Main file for the advent_of_code2017 repository

To use this run 'py advent_of_code *day* *part*', where
- day is an integer number between 1 and 25,
- and part is an optional integer number between 1 and 2

Run 'py -m unittest discover tests' to also run the tests for this project

Author: Ic4r0 - https://github.com/Ic4r0

Created: 11th February 2023
"""

# imports
import sys

from days.day_2 import day_2
from days.day_1 import day_1
from utils.validator import check_valid_arguments


def save_xmas(selected_day: int, selected_part: int = None):
    """ Needed to select the correct module corresponding to the selected day
    :param selected_day: selected Advent of Code day
    :param selected_part: selected Advent of Code part of the selected day
    """
    if selected_day == 1:
        day_1(selected_part)
    elif selected_day == 2:
        day_2(selected_part)
    elif 0 < selected_day < 26:
        print('No available solution for the selected day')
    else:
        print('Choose a day between 1 and 25')


if __name__ == "__main__":
    day = None
    part = None

    arguments = check_valid_arguments(sys.argv[1:])
    if arguments:
        day, part = arguments
        save_xmas(day, part)
    else:
        print('To use this run \'python advent_of_code *day* *part*\', where day is an integer number between 1 '
              'and 25, and part is an optional integer number between 1 and 2')
