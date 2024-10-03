import unittest
import math

def calculate_sqlt_number(input_number, random_number):
    try:
        input_number = int(input_number)
    except ValueError:
        print("Введенное значение не является целым числом")
        return None

    difference_numbers = input_number - random_number
    print(f'{input_number} - ({random_number}) = {difference_numbers}')
    if difference_numbers >= 0:
        sqlt_number = round(math.sqrt(difference_numbers), 2)
        print(f'Корень из {difference_numbers} = {sqlt_number}')
        return sqlt_number
    else:
        print(f'Корень из {difference_numbers} не существует, т.к. число отрицательное')
        return None

class TestCalculateSqltNumber(unittest.TestCase):

    def test_positive_difference(self):
        input_number = 5
        random_number = 3
        difference_numbers = input_number - random_number
        expected_sqlt_number = round(math.sqrt(difference_numbers), 2)
        self.assertAlmostEqual(calculate_sqlt_number(input_number, random_number), expected_sqlt_number)

    def test_negative_difference(self):
        input_number = 3
        random_number = 5
        self.assertIsNone(calculate_sqlt_number(input_number, random_number))

    def test_zero_difference(self):
        input_number = 5
        random_number = 5
        expected_sqlt_number = 0.00
        self.assertAlmostEqual(calculate_sqlt_number(input_number, random_number), expected_sqlt_number)

    def test_invalid_input(self):
        input_number = 'five'
        random_number = 5
        self.assertIsNone(calculate_sqlt_number(input_number, random_number))

if __name__ == '__main__':
    unittest.main()