import pytest
from src.module_12 import m_12_9_1, m_12_9_2, m_12_9_3, m_12_9_4


# m_12_9_1: Префиксный генератор через замыкание
@pytest.mark.parametrize(
    "prefix, text, expected",
    [
        ("DEBUG: ", "Hello", "DEBUG: Hello"),
        ("[INFO] ", "World", "[INFO] World"),
        ("🚀 ", "Python", "🚀 Python"),
        ("", "no prefix", "no prefix"),  # Пустой префикс
        ("END: ", "", "END: "),  # Пустая строка
    ],
)
def test_12_9_1(prefix, text, expected):
    result = m_12_9_1(prefix, text)
    assert result == expected


# m_12_9_2: Генератор функций возведения в степень через замыкание
@pytest.mark.parametrize(
    "base, ex, expected",
    [
        (2, 3, 8),  # 2³ = 8
        (5, 2, 25),  # 5² = 25
        (3, 4, 81),  # 3⁴ = 81
        (10, 0, 1),  # Любое число в 0 степени = 1
        (7, 1, 7),  # x¹ = x
    ],
)
def test_12_9_2(base, ex, expected):
    result = m_12_9_2(base, ex)
    assert result == expected


# m_12_9_3: Создание счетчика через замыкание
def test_12_9_3():
    counter = m_12_9_3()  # Получаем счетчик

    assert counter() == 1  # Первый вызов → 1
    assert counter() == 2  # Второй → 2
    assert counter() == 3  # Третий → 3
    for _ in range(6):
        counter()
    assert counter() == 10  # Десятый → 10


# m_12_9_4: Аккумулятор суммы через замыкание
@pytest.mark.parametrize(
    "values, expected_total",
    [
        ([5, 10, -3, 12, -5, 0, -5], 14),  # Sample Input → 14
        ([1, 1, 1, 1], 4),  # Простая сумма → 4
        ([-1, -1, -1], -3),  # Отрицательные → -3
        ([100, -50, 25], 75),  # Смешанные → 75
        ([100, -50, -50], 0),  # Нулевая сумма
    ],
)
def test_12_9_4(values, expected_total):
    accumulator = m_12_9_4()
    for value in values:
        accumulator(value)
    res = accumulator(0)
    accumulator(-res)  # обнуляем сумму
    assert res == expected_total
