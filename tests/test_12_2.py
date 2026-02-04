import pytest
from src.module_12 import (
    m_12_2_1,
    m_12_2_2,
    m_12_2_3,
    m_12_2_4,
    m_12_2_5,
    m_12_2_6,
    m_12_2_7,
    m_12_2_8,
    m_12_2_9,
    m_12_2_10,
    m_12_2_11,
    m_12_2_12,
    m_12_2_13,
    m_12_2_14,
    m_12_2_15,
    m_12_2_16,
)


# m_12_2_1: Функция приветствие
@pytest.mark.parametrize(
    "expected",
    [
        "Hello, world!",
    ],
)
def test_12_2_1(expected, capsys):
    m_12_2_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


# m_12_2_2: Функция приветствие 2
@pytest.mark.parametrize(
    "name, expected",
    [
        ("Arthur", "Hello, Arthur!"),
        ("Alice", "Hello, Alice!"),
        ("", "Hello, !"),
        ("Vsevolod", "Hello, Vsevolod!"),
    ],
)
def test_12_2_2(name, expected, capsys):
    m_12_2_2(name)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


# m_12_2_3: Функция приветствие 3
@pytest.mark.parametrize(
    "name, expected",
    [
        ("Arthur", "Hello, Arthur!"),
        (None, "Hello, unknown!"),  # Параметр по умолчанию
        ("", "Hello, !"),
        ("Vsevolod", "Hello, Vsevolod!"),
    ],
)
def test_12_2_3(name, expected, capsys):
    m_12_2_3(name)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


# m_12_2_4: Функция суммы двух чисел
@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (1, 2, 3),
        (0, 0, 0),
        (-1, 1, 0),
        (5.5, 3.2, 8.7),
    ],
)
def test_12_2_4(num1, num2, expected):
    result = m_12_2_4(num1, num2)
    assert result == expected


# m_12_2_5: Функция суммы чисел
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3], 6),
        ([], 0),
        ([5.5, 3.2], 8.7),
        ([10], 10),
    ],
)
def test_12_2_5(nums, expected):
    result = m_12_2_5(nums)
    assert result == expected


# m_12_2_6: Вычисление квадрата числа
@pytest.mark.parametrize(
    "num, expected",
    [
        (4.0, 16.0),
        (0.0, 0.0),
        (-2.5, 6.25),
        (1.5, 2.25),
    ],
)
def test_12_2_6(num, expected):
    result = m_12_2_6(num)
    assert result == expected


# m_12_2_7: Функция большее из двух чисел
@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (1, 2, 2),
        (5, 5, 5),
        (-1, 10, 10),
        (3.2, 2.1, 3.2),
    ],
)
def test_12_2_7(num1, num2, expected):
    result = m_12_2_7(num1, num2)
    assert result == expected


# m_12_2_8: Сумма в диапазоне
@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (1, 4, 10),  # 1+2+3+4
        (5, 3, 12),  # Меняются местами: 3+4+5
        (-1, 1, 0),  # -1+0+1
        (0, 0, 0),  # Один элемент
    ],
)
def test_12_2_8(num1, num2, expected):
    result = m_12_2_8(num1, num2)
    assert result == expected


# m_12_2_9: Чётность
@pytest.mark.parametrize(
    "num, expected",
    [
        (4, True),
        (3, False),
        (0, True),  # 0 чётное
        (-2, True),  # Отрицательные тоже
    ],
)
def test_12_2_9(num, expected):
    result = m_12_2_9(num)
    assert result == expected


# m_12_2_10: Високосный год
@pytest.mark.parametrize(
    "year, expected",
    [
        (2024, True),  # %4==0 и не %100==0
        (1900, False),  # %100==0 но не %400==0
        (2000, True),  # %400==0
        (2023, False),
    ],
)
def test_12_2_10(year, expected):
    result = m_12_2_10(year)
    assert result == expected


# m_12_2_11: Треугольник
@pytest.mark.parametrize(
    "len1, len2, len3, expected",
    [
        (3, 4, 5, True),  # Обычный
        (1, 1, 1, True),  # Равносторонний
        (1, 1, 3, False),  # НЕ треугольник: 1+1≯3
        (5, 5, 11, False),  # Граничный случай
    ],
)
def test_12_2_11(len1, len2, len3, expected):
    result = m_12_2_11(len1, len2, len3)
    assert result == expected


# m_12_2_12: Максимум из *args
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 3, 2], 3),
        ([], float("-inf")),  # Пустой список
        ([-1, -5, 0], 0),
        ([10.5], 10.5),  # Один элемент
    ],
)
def test_12_2_12(nums, expected):
    result = m_12_2_12(nums)
    assert result == expected


# m_12_2_13: Произведение *args
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([2, 3, 4], 24),
        ([5], 5),  # Один элемент
        ([-2, 3], -6),
        ([1, 1, 1], 1),
    ],
)
def test_12_2_13(nums, expected):
    result = m_12_2_13(nums)
    assert result == expected


# m_12_2_14: Произведение *args + start
@pytest.mark.parametrize(
    "nums, num, expected",
    [
        ([2, 3], 2, 12),  # 2*2*3
        ([5], 0, 0),  # 0*5
        ([], 10, 10),  # Пустой *args: только start
        ([-1, 2], 3, -6),  # 3*-1*2
    ],
)
def test_12_2_14(nums, num, expected):
    result = m_12_2_14(nums, num)
    assert result == expected


# m_12_2_15: Функция по смещению символа
@pytest.mark.parametrize(
    "ch, shift, expected",
    [
        ("y", 3, "b"),
        ("B", -3, "Y"),
        # Обычный случай
        ("k", 3, "n"),  # k→l→m→n
        # Пограничные случаи
        ("z", 1, "a"),  # z→a (закольцовка нижний)
        ("Z", -1, "Y"),  # Z→Y (отрицательный верхний)
        ("a", -2, "y"),  # a→z→y (отрицательный с закольцовкой)
        # Большие сдвиги (>40)
        ("a", 42, "q"),  # 42 % 26 = 16 → a+16=q
        ("Z", -53, "Y"),  # -53 % 26 = 1 → Z-1=Y
    ],
)
def test_12_2_15(ch, shift, expected):
    result = m_12_2_15(ch, shift)
    assert result == expected


# m_12_2_16: Шифр Цезаря и дешифровка
@pytest.mark.parametrize(
    "data, num, expected",
    [
        # Sample Input 1
        ("Hello, world!", 3, "Khoor, zruog!"),
        # Sample Input 2
        ("Khoor, zruog!", -3, "Hello, world!"),
        # 1. Простой тест
        ("abc", 1, "bcd"),
        # 2. Пограничный: закольцовка
        ("xyz", 3, "abc"),
        # 3. Пограничный: отрицательный сдвиг
        ("ABC", -1, "ZAB"),
        # 4. Большой сдвиг
        ("Test", 42, "Juij"),  # 42 % 26 = 16
    ],
)
def test_12_2_16(data, num, expected):
    result = m_12_2_16(data, num)
    assert result == expected
