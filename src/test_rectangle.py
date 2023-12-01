import pytest
from src.Rectangle import Rectangle

def test_rectangle_with_positive_numbers():
    # Проверяем, что класс корректно обрабатывает положительные числа
    rect = Rectangle(3, 4)
    assert rect.name == "Rectangle 3 and 4"

def test_rectangle_with_non_number_sides():
    # Проверяем, что класс выдаёт ошибку, если передан нечисловой аргумент
    with pytest.raises(ValueError):
        Rectangle("three", 4)
    with pytest.raises(ValueError):
        Rectangle(3, "four")

def test_rectangle_with_non_positive_sides():
    # Проверяем, что класс выдаёт ошибку для отрицательных чисел и нуля
    with pytest.raises(ValueError):
        Rectangle(-1, 2)
    with pytest.raises(ValueError):
        Rectangle(2, -1)
    with pytest.raises(ValueError):
        Rectangle(0, 2)
    with pytest.raises(ValueError):
        Rectangle(1, 0)

def test_rectangle_with_floats():
    # Проверяем, что класс корректно обрабатывает числа с плавающей точкой
    rect = Rectangle(1.5, 3.5)
    assert rect.name == "Rectangle 1.5 and 3.5"