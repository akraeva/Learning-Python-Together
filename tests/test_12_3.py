import pytest
from src.module_12 import m_12_3_1, m_12_3_2


# m_12_3_1: Меняем глобальную переменную
@pytest.mark.parametrize(
    "num, expected_x",
    [
        (5, 15),  # Положительное
        (-3, 7),  # Отрицательное
        (0, 10),  # Ноль
        (-10, 0),  # Из нуля
    ],
)
def test_m_12_3_1(num, expected_x):
    result = m_12_3_1(num)
    m_12_3_1(-num)
    assert result == expected_x


# m_12_3_2: Меняем локальную переменную
@pytest.mark.parametrize(
    "num, expected",
    [
        (5, 15),  # 10 + 5
        (-3, 7),  # 10 - 3
        (0, 10),  # 10 + 0
        (25, 35),  # 10 + 25
    ],
)
def test_m_12_3_2(capfd, num, expected):
    m_12_3_2(num)
    captured = capfd.readouterr()
    assert captured.out.strip() == str(expected)
