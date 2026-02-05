import pytest
from src.module_12 import m_12_4_1, m_12_4_2, m_12_4_3, m_12_4_4


# m_12_4_1: Генератор диапазона чисел
@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 5, [1, 2, 3, 4, 5]),
        (0, 3, [0, 1, 2, 3]),
        (-2, 0, [-2, -1, 0]),
        (5, 5, [5]),  # start == stop
    ],
)
def test_m_12_4_1(start, stop, expected):
    gen = m_12_4_1(start, stop)
    assert list(gen) == expected


# m_12_4_2: Генератор чисел в квадрате
@pytest.mark.parametrize(
    "steps, expected",
    [
        (0, []),  # 0 итераций
        (2, [0, 1]),
        (1, [0]),  # 0²
        (4, [0, 1, 4, 9]),  # 0²,1²,2²,3²
        (6, [0, 1, 4, 9, 16, 25]),  # Больше
    ],
)
def test_m_12_4_2(steps, expected):
    gen = m_12_4_2()
    result = [next(gen) for _ in range(steps)]
    assert result == expected


# m_12_4_3: Генератор факториалов
@pytest.mark.parametrize(
    "n, expected",
    [
        (1, [1]),
        (2, [1, 2]),
        (3, [1, 2, 6]),
        (5, [1, 2, 6, 24, 120]),
        (7, [1, 2, 6, 24, 120, 720, 5040]),
    ],
)
def test_m_12_4_3(n, expected):
    gen = m_12_4_3()
    result = [next(gen) for _ in range(n)]
    assert result == expected


# m_12_4_4: Генератор чисел Фибоначчи


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, [0]),  # F(0) = 0
        (3, [0, 1, 1]),  # F(0),F(1),F(2)
        (6, [0, 1, 1, 2, 3, 5]),  # F(0)..F(5)
        (8, [0, 1, 1, 2, 3, 5, 8, 13]),  # F(0)..F(7)
        (0, []),  # 0 итераций
    ],
)
def test_m_12_4_4(n, expected):
    gen = m_12_4_4()
    result = [next(gen) for _ in range(n)]
    assert result == expected
