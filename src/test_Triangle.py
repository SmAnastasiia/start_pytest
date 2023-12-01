import pytest
from src.Triangle import Triangle

# Тест: Инициализация с положительными сторонами, удовлетворяющими неравенству треугольника
def test_triangle_initialization_valid():
    triangle = Triangle(3, 4, 5)
    assert triangle.side_a == 3
    assert triangle.side_b == 4
    assert triangle.side_c == 5
    assert triangle.name == "Triangle 3 and 4 and 5"

# Тест: Исключение при инициализации с отрицательными сторонами
def test_triangle_initialization_with_negative_sides_raises_error():
    with pytest.raises(ValueError):
        Triangle(-3, 4, 5)

# Тест: Исключение при инициализации с нулевыми сторонами
def test_triangle_initialization_with_zero_sides_raises_error():
    with pytest.raises(ValueError):
        Triangle(0, 0, 0)

# Тест: Исключение при инициализации с невалидным набором сторон (нарушение неравенства треугольника)
def test_triangle_initialization_invalid_sides_raises_error():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)

# Тест: Вычисление площади треугольника
def test_triangle_area_calculation():
    triangle = Triangle(3, 4, 5)
    expected_area = 6.0  # Площадь прямоугольного треугольника со сторонами 3, 4, 5
    assert triangle.get_area == expected_area

# Тест: Вычисление периметра треугольника
def test_triangle_perimeter_calculation():
    triangle = Triangle(3, 4, 5)
    expected_perimeter = 12  # Периметр треугольника со сторонами 3, 4, 5
    assert triangle.get_perimeter == expected_perimeter
