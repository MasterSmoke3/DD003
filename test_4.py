import unittest

def process_integer_input(input_int):
    """Вспомогательная функция для имитации обработки целого числа."""
    if input_int.isdigit():
        return f'Твое число в степени два равно {int(input_int)**2}'
    else:
        return 'Ну я же просил ввести целое число! Ну камон!'

def process_string_input(input_str):
    """Вспомогательная функция для имитации обработки строки."""
    if input_str.isdigit():
        return f'Вы ввели число {input_str}'
    else:
        return f'{input_str} - это не число'

class TestInputValidation(unittest.TestCase):

    def test_valid_integer_input(self):
        """Проверяет обработку корректного целого числа."""
        user_input = "123"
        expected_output = "Твое число в степени два равно 15129"
        self.assertEqual(process_integer_input(user_input), expected_output)

    def test_invalid_integer_input(self):
        """Проверяет обработку некорректного целого числа."""
        user_input = "abc"
        expected_output = "Ну я же просил ввести целое число! Ну камон!"
        self.assertEqual(process_integer_input(user_input), expected_output)

    def test_valid_string_input(self):
        """Проверяет обработку корректной строки с числом и буквой."""
        user_input = "123a"
        expected_output = "123a - это не число"
        self.assertEqual(process_string_input(user_input), expected_output)

    def test_valid_integer_string_input(self):
        """Проверяет обработку корректной строки с числом."""
        user_input = "123"
        expected_output = "Вы ввели число 123"
        self.assertEqual(process_string_input(user_input), expected_output)

if __name__ == '__main__':
    unittest.main()