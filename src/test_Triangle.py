import pytest
from src.Triangle import Triangle

"""Инициализация с положительными сторонами, удовлетворяющими неравенству треугольника"""
def test_triangle_initialization_valid():
    triangle = Triangle(3, 4, 5)
    assert triangle.side_a == 3
    assert triangle.side_b == 4
    assert triangle.side_c == 5
    assert triangle.name == "Triangle 3 and 4 and 5"

@pytest.mark.parametrize("a, b, c", [
    (-3, 4, 5),  # negative sides
    (0, 0, 0),   # zero sides
    (1, 2, 3)    # invalid sides
])
def test_triangle_initialization_raises_error(a, b, c):
    with pytest.raises(ValueError):
        Triangle(a, b, c)


"""Вычисление площади треугольника"""
def test_triangle_area_calculation():
    triangle = Triangle(3, 4, 5)
    expected_area = 6.0  # Площадь прямоугольного треугольника со сторонами 3, 4, 5
    assert triangle.get_area == expected_area

"""Вычисление периметра треугольника"""
def test_triangle_perimeter_calculation():
    triangle = Triangle(3, 4, 5)
    expected_perimeter = 12  # Периметр треугольника со сторонами 3, 4, 5
    assert triangle.get_perimeter == expected_perimeter
