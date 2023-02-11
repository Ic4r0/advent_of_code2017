import unittest
from days.day_1 import day_1


class TestDays(unittest.TestCase):
    def test_day_1(self):
        """Test 1st day"""
        self.assertEqual((9, 6), day_1(None, True))


if __name__ == '__main__':
    unittest.main()
