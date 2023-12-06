import pytest
from src.Rectangle import Rectangle

def test_rectangle_with_positive_numbers():
    """Проверяем, что класс корректно обрабатывает положительные числа"""
    rect = Rectangle(3, 4)
    assert rect.name == "Rectangle 3 and 4"

def test_rectangle_with_string_as_width():
    """Проверяем, что класс выдаёт ошибку, если первый аргумент не число"""
    with pytest.raises(ValueError):
        Rectangle("three", 4)

def test_rectangle_with_string_as_height():
    """Проверяем, что класс выдаёт ошибку, если второй аргумент не число"""
    with pytest.raises(ValueError):
        Rectangle(3, "four")

def test_rectangle_with_negative_width():
    """Проверяем, что класс выдаёт ошибку для отрицательной ширины"""
    with pytest.raises(ValueError):
        Rectangle(-1, 2)

def test_rectangle_with_negative_height():
    """Проверяем, что класс выдаёт ошибку для отрицательной высоты"""
    with pytest.raises(ValueError):
        Rectangle(2, -1)

def test_rectangle_with_zero_width():
    """Проверяем, что класс выдаёт ошибку для нулевой ширины"""
    with pytest.raises(ValueError):
        Rectangle(0, 2)

def test_rectangle_with_zero_height():
    """Проверяем, что класс выдаёт ошибку для нулевой высоты"""
    with pytest.raises(ValueError):
        Rectangle(1, 0)


def test_rectangle_with_floats():
    """Проверяем, что класс корректно обрабатывает числа с плавающей точкой"""
    rect = Rectangle(1.5, 3.5)
    assert rect.name == "Rectangle 1.5 and 3.5"