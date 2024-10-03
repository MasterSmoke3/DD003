import unittest
from unittest.mock import patch
from io import StringIO
import sys

def index_visualization():
    test_string = 'Тестовая строчка'
    print(test_string)

    is_index_flag = bool(int(input('\nВведи\n - 0, если хочешь прекратить программу;\n - 1, если хочешь задать индекс.\n')))

    if is_index_flag:
        index = int(input('Введи индекс: '))
        if 0 <= index < len(test_string):
            print(f'Элемент, стоящий под этим индексом - "{test_string[index]}"')
        else:
            print('Индекс вне диапазона строки')
    else:
        sys.exit()

class TestIndexVisualization(unittest.TestCase):

    def test_valid_index(self):
        test_string = 'Тестовая строчка'
        index = 3
        expected_output = f'Элемент, стоящий под этим индексом - "{test_string[index]}"\n'
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            with patch('builtins.input', side_effect=['1', str(index)]):
                index_visualization()
                self.assertEqual(mock_stdout.getvalue(), test_string + '\n' + expected_output)

    def test_invalid_index(self):
        test_string = 'Тестовая строчка'
        index = 20
        expected_output = 'Индекс вне диапазона строки\n'
        with patch('sys.stdout', new=StringIO()) as mock_stdout:
            with patch('builtins.input', side_effect=['1', str(index)]):
                index_visualization()
                self.assertEqual(mock_stdout.getvalue(), test_string + '\n' + expected_output)

    def test_exit_program(self):
        with patch('builtins.input', side_effect=['0']):
            with self.assertRaises(SystemExit):
                index_visualization()

if __name__ == '__main__':
    unittest.main()