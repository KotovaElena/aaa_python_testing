from one_hot_encoder import fit_transform
import unittest


class TestFitTransform(unittest.TestCase):
    """Класс для тестирования функции fit_transform из one_hot_encoder.py"""

    def test_positive(self):
        """Тест на корректность вывода для входных данных в виде списка"""
        cities = ['Moscow', 'New York', 'Moscow', 'London']
        actual = fit_transform(cities)
        expected = [
            ('Moscow', [0, 0, 1]),
            ('New York', [0, 1, 0]),
            ('Moscow', [0, 0, 1]),
            ('London', [1, 0, 0]),
        ]
        self.assertEqual(actual, expected)

    def test_one_string(self):
        """Тест на корректность вывода для входных данных в виде одной строки"""
        cities = 'Belgorod'
        actual = fit_transform(cities)
        expected = [('Belgorod', [1])]
        self.assertEqual(actual, expected)

    def test_empty(self):
        """Тест для входных данных в виде пустого списка"""
        cities = []
        actual = fit_transform(cities)
        self.assertFalse(actual)

    def test_type_error(self):
        """Тест для входных данных типа int"""
        cities = 1
        with self.assertRaises(TypeError):
            fit_transform(cities)
