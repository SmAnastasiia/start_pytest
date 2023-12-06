import pytest
from src.Figure import Figure
from Circle import Circle
import math

def test_create_circle():
    radius = 5
    circle = Circle(radius)
    assert circle.radius == radius
    assert circle.name == f"Circle {radius}"

"""Выброс исключения при радиусе равном нулю"""
def test_create_circle_with_zero_radius():
    with pytest.raises(ValueError):
        Circle(0)

"""Выброс исключения при отрицательном радиусе"""
def test_create_circle_with_negative_radius():
    with pytest.raises(ValueError):
        Circle(-1)


""""Тест на проверку того, что радиус должен быть числом"""
def test_create_circle_with_non_number_radius():
    with pytest.raises(ValueError):
        Circle("a")

""""Тесты для проверки площади"""
def test_circle_area():
    radius = 2
    circle = Circle(radius)
    assert circle.get_area == round(math.pi * radius ** 2, 2)

"""Тесты для проверки периметра (или окружности)"""
def test_circle_perimeter():
    radius = 2
    circle = Circle(radius)
    assert circle.get_perimeter == round(2 * math.pi * radius, 2)