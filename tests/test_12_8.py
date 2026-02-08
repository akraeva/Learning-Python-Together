import pytest
from src.module_12 import (
    m_12_8_1,
    m_12_8_2,
    m_12_8_3,
    m_12_8_4,
)


# m_12_8_1: Факториал через рекурсию
@pytest.mark.parametrize(
    "num, expected",
    [
        (5, 120),  # Sample Input
        (1, 1),  # Факториал 1! = 1
        (7, 5040),  # Факториал 7! = 5040
        (10, 3628800),  # Большее число
        (0, 1),  # Факториал 0! = 1
    ],
)
def test_12_8_1(num, expected):
    result = m_12_8_1(num)
    assert result == expected


# m_12_8_2: Числа Фибоначчи через рекурсию
@pytest.mark.parametrize(
    "num, expected",
    [
        (2, 1),  # Sample Input
        (0, 0),  # F(0) = 0
        (1, 1),  # F(1) = 1
        (5, 5),  # F(5) = 5
        (7, 13),  # Большее число
    ],
)
def test_12_8_2(num, expected):
    result = m_12_8_2(num)
    assert result == expected


# m_12_8_3: Сумма цифр числа через рекурсию
@pytest.mark.parametrize(
    "num, expected",
    [
        (123, 6),  # Sample Input (1+2+3=6)
        (0, 0),  # Ноль
        (999, 27),  # Максимум цифр (9+9+9=27)
        (100, 1),  # С нулями
        (7, 7),  # Одна цифра
    ],
)
def test_12_8_3(num, expected):
    result = m_12_8_3(num)
    assert result == expected


# m_12_8_4: Палиндром через рекурсию
@pytest.mark.parametrize(
    "line, expected",
    [
        ("топот", True),  # Sample Input
        ("", True),  # Пустая строка
        ("a", True),  # Одна буква
        ("abc", False),  # Обычная строка
        ("abba", True),  # Симметричный палиндром
    ],
)
def test_12_8_4(line, expected):
    result = m_12_8_4(line)
    assert result == expected
