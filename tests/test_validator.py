""" Test class for validator module
Author: Ic4r0 - https://github.com/Ic4r0
Created: 11th February 2023
"""
import unittest
from utils.validator import check_valid_arguments


class TestValidator(unittest.TestCase):
    def test_full(self):
        """Test validator: 1, 1"""
        self.assertEqual(
            (1, 1),
            check_valid_arguments(['1', '1'])
        )

    def test_partial_test(self):
        """Test validator: 1"""
        self.assertEqual(
            (1, None),
            check_valid_arguments(['1'])
        )

    def test_wrong_inputs(self):
        """Test validator: 'Not valid'"""
        self.assertEqual(
            None,
            check_valid_arguments(['Not valid'])
        )

    def test_no_inputs(self):
        """Test validator: []"""
        self.assertEqual(
            None,
            check_valid_arguments([])
        )


if __name__ == '__main__':
    unittest.main()
