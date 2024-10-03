import unittest
class TestStringManipulation(unittest.TestCase):

    def test_string_manipulation(self):
        """Проверяет манипуляции со строками."""
        string = ' I like administration of hospital   '
        exclamation_point = '!'
        exclamation_point *= 3
        string = string.strip()
        string = string[:12].upper()
        expected_output = f'{string}{exclamation_point} Ох, так неожиданно и прияяятноооо.'
        self.assertEqual(expected_output, "I LIKE ADMIN!!! Ох, так неожиданно и прияяятноооо.")
if __name__ == '__main__':
    unittest.main()