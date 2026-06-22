import unittest
from find_minimum_in_rotated_array import findMin

class TestFindMinInRotatedArray(unittest.TestCase):
    def test_example1(self):
        # The original array was [1,2,3,4,5] rotated 3 times.
        self.assertEqual(findMin([3, 4, 5, 1, 2]), 1)

    def test_example2(self):
        # The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
        self.assertEqual(findMin([4, 5, 6, 7, 0, 1, 2]), 0)

    def test_example3(self):
        # The original array was [11,13,15,17] and it was rotated 4 times.
        self.assertEqual(findMin([11, 13, 15, 17]), 11)

if __name__ == '__main__':
    unittest.main()
