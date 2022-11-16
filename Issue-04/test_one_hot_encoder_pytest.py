from one_hot_encoder import fit_transform
import pytest


def test_positive():
    """Тест на корректность вывода для входных данных в виде списка"""
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    actual = fit_transform(cities)
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert actual == expected


def test_empty():
    """Тест для входных данных в виде пустого списка"""
    cities = []
    actual = fit_transform(cities)
    expected = []
    assert actual == expected


def test_type_error():
    """Тест для входных данных типа int"""
    cities = 1
    with pytest.raises(TypeError):
        fit_transform(cities)


def test_len():
    """Тест на соответсвие длины входных и выходных данных"""
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    actual = fit_transform(cities)
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert len(actual) == len(expected)
