import pytest
from src.module_12 import m_12_10_1, m_12_10_2, m_12_10_3


# m_12_10_1: Создание декоратора для валидации положительных целочисленных значений
@pytest.mark.parametrize(
    "args, expected",
    [
        (
            (0, 1, "Two"),
            "Все аргументы должны быть целочисленные и положительные числа!",
        ),
        ((1, 2), 3),  # Положительные int → OK
        (
            (1, -1),
            "Все аргументы должны быть целочисленные и положительные числа!",
        ),  # Отрицательное → ошибка
        (
            (1.5, 2),
            "Все аргументы должны быть целочисленные и положительные числа!",
        ),  # Float → ошибка
        (
            (0, 1),
            "Все аргументы должны быть целочисленные и положительные числа!",
        ),  # Ноль → ошибка
        (
            (1, True),
            "Все аргументы должны быть целочисленные и положительные числа!",
        ),  # Ноль → ошибка
    ],
)
def test_12_10_1(args, expected):
    def test_func(a, b):  # Тестируемая функция
        return a + b

    decorated = m_12_10_1(test_func)
    result = decorated(*args)  # Вызываем декорированную функцию
    assert result == expected


# m_12_10_2: Создание декоратора для кеширования результатов функции
@pytest.mark.parametrize(
    "args_list, expected_results",
    [
        # Повтор факториала 5! = 120 (кеш сработает во 2-м вызове)
        ([(5,), (5,), (3,)], [120, 120, 6]),
        # Короткие: 0!=1 (база), 1!=1 (база), 2!=2 (новое)
        ([(0,), (1,), (2,), (1,)], [1, 1, 2, 1]),
        # Большие с кешем: 6!=720 дважды + 4!=24
        ([(6,), (6,), (4,)], [720, 720, 24]),
        # Граничный: 1 (кеш), 0 (база), 3!=6
        ([(1,), (0,), (3,), (1,)], [1, 1, 6, 1]),
    ],
)
def test_12_10_2(args_list, expected_results):
    def test_func(n):
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    cached_func = m_12_10_2(test_func)

    results = []
    for args in args_list:
        results.append(cached_func(*args))

    assert results == expected_results


# m_12_10_3: Декоратор с параметром для повторения выполнения функции
@pytest.mark.parametrize(
    "times, expected_calls",
    [
        (3, 3),
        (1, 1),
        (0, 0),
        (5, 5),
    ],
)
def test_12_10_3(times, expected_calls):
    call_counter = 0  # Счётчик побочных эффектов

    def test_func(*args):
        nonlocal call_counter
        call_counter += 1  # Side-effect

    repeat_factory = m_12_10_3()
    decorator = repeat_factory(times)
    repeated_func = decorator(test_func)

    repeated_func()  # Вызов

    assert call_counter == expected_calls
