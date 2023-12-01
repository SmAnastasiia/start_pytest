import pytest
from src.Figure import Figure
from src.Square import Square

def test_square_initialization_with_positive_number():
    # Проверяем, правильно ли создается квадрат с положительной длиной стороны
    side = 3
    square = Square(side)
    assert square.side == side
    assert square.name == f"Square {side}"

def test_square_initialization_with_negative_number_raises_error():
    # Проверяем, вызовет ли ошибка инициализация с отрицательной длиной стороны
    with pytest.raises(ValueError):
        Square(-1)

def test_square_initialization_with_zero_raises_error():
    # Проверяем, вызовет ли ошибка инициализация с нулевой длиной стороны
    with pytest.raises(ValueError):
        Square(0)

def test_square_initialization_with_non_number_raises_error():
    # Проверяем, вызовет ли ошибка инициализация с аргументом не числового типа
    with pytest.raises(ValueError):
        Square('three')

def test_square_area_calculation():
    # Проверяем правильность вычисления площади
    side = 3
    square = Square(side)
    expected_area = side * 2
    assert square.get_area == expected_area

def test_square_perimeter_calculation():
    # Проверяем правильность вычисления периметра
    side = 3
    square = Square(side)
    expected_perimeter = side * 4
    assert square.get_perimeter == expected_perimeter
