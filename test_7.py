import unittest

class TestStringSlicing(unittest.TestCase):

    def test_valid_slice(self):
        test_string = 'Тестовая строчка'
        self.assertEqual(test_string[2:6:1], 'стов' )

    def test_slice_from_beginning(self):
        test_string = 'Тестовая строчка'
        self.assertEqual(test_string[:6:1], 'Тестов')

    def test_slice_to_end(self):
        test_string = 'Тестовая строчка'
        self.assertEqual(test_string[2::1], 'стовая строчка')

    def test_slice_with_step(self):
        test_string = 'Тестовая строчка'
        self.assertEqual(test_string[2:8:2], 'соа')

    def test_negative_step(self):
        test_string = 'Тестовая строчка'
        self.assertEqual(test_string[10:2:-1], 'тс яавот')

    def test_invalid_slice(self):
        test_string = 'Тестовая строчка'
        with self.assertRaises(TypeError):
            test_string[2:6:"invalid"]

    def test_start_greater_than_end(self):
        test_string = 'Тестовая строчка'
        self.assertEqual(test_string[6:2:1], "") 

if __name__ == '__main__':
    unittest.main()