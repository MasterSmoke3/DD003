import unittest

class TestCalculations(unittest.TestCase):
    def test_calculations(self):
        num_1 = 3
        num_2 = num_1 ** 2 + 10 / 5
        num_3 = num_1 + num_2 % 2 + 1
        num_4 = num_1 // 3 + num_3
        self.assertEqual(num_4, 6)
if __name__ == '__main__':
    unittest.main()