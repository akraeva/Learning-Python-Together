import pytest
from src.module_11 import (
    m_11_3_1,
    m_11_3_2,
    m_11_3_3,
    m_11_3_4,
    m_11_3_5,
    m_11_3_6,
    m_11_3_7,
)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        # Sample Input 1
        ("2", "2"),
        # Sample Input 2
        ("5,0", "Ошибка ввода числа"),
        # Дополнительные случаи
        ("abc", "Ошибка ввода числа"),  # Буквы
        ("3.14", "Ошибка ввода числа"),  # Дробное
        ("123", "123"),  # Много цифр
        ("-5", "-5"),  # Отрицательное
        ("", "Ошибка ввода числа"),  # Пустая строка
        ("  42  ", "42"),  # С пробелами
    ],
)
def test_11_3_1(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_11_3_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        # Sample Input 1: 10 / 2 = 5.0
        ("10\n2", "5.0"),
        # Sample Input 2: 1 / 0 → ZeroDivisionError
        ("1\n0", "На ноль делить нельзя!"),
        # Дополнительные случаи
        ("15\n3", "5.0"),  # Красивое деление
        ("7\n2", "3.5"),  # Дробный результат
        ("0\n5", "0.0"),  # 0 на число
        ("-10\n2", "-5.0"),  # Отрицательное делимое
        ("10\n-2", "-5.0"),  # Отрицатель разность
    ],
)
def test_11_3_2(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_11_3_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        # Sample Input 1: ValueError (буквы)
        ("2\ndfg", "Должны быть числа, а не строки!"),
        # Sample Input 2: ZeroDivisionError
        ("1\n0", "На ноль делить нельзя!"),
        # Дополнительные случаи
        ("abc\ndef", "Должны быть числа, а не строки!"),  # Оба - буквы
        ("10\nabc", "Должны быть числа, а не строки!"),  # Второй - буквы
        ("10\n2", "5.0"),  # Нормальное деление
        ("15\n0", "На ноль делить нельзя!"),  # Деление на 0
        ("-5\n2", "-2.5"),  # Отрицательное
        ("0\n10", "0.0"),  # 0 на число
        ("3.14\n2", "Должны быть числа, а не строки!"),  # Дробное число
    ],
)
def test_11_3_3(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_11_3_3()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        # Sample Input (сумма корректных: 1+3+5+11=20)
        (
            "1\n3\n5\na\nb9\n11\nx13",
            "20",
        ),
        # Только корректные числа
        (
            "10\n20\n30",
            "60",
        ),
        # Только ошибки
        (
            "abc\ndef\nxyz",
            "0",
        ),
        # Смешанные + отрицательные
        (
            "1\n-2\nabc\n3\ndef\n-4",
            "-2",
        ),
        # Один корректный
        (
            "42\nerror\nspam",
            "42",
        ),
        # Пустая последовательность (EOF сразу)
        (
            "",
            "0",
        ),
    ],
)
def test_11_3_4(inputs, expected, mocker, capsys):
    # EOFError симуляция: input() → StopIteration
    def mock_input():
        lines = inputs.split("\n")
        for line in lines:
            yield line
        raise EOFError

    mocker.patch("builtins.input", side_effect=mock_input())
    m_11_3_4()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        # Sample Input 1: список [0,1,2,3,4,5,6,7,8,9], индекс 5 → 5
        ("0 1 2 3 4 5 6 7 8 9\n5", "5"),
        # Sample Input 2: список [3,6,9], индекс 3 → IndexError
        ("3 6 9\n3", "Запрашиваемый индекс выходит на пределы списка!"),
        # Дополнительные случаи
        ("1 2 3\n0", "1"),  # Первый элемент
        (
            "97 98 99\n0",
            "97",
        ),  # Пустой список
        (
            "10\n1",
            "Запрашиваемый индекс выходит на пределы списка!",
        ),  # Индекс 0 на списке длины 1
        ("1 2 3 4\n2", "3"),  # Средний элемент
        ("5\n10", "Запрашиваемый индекс выходит на пределы списка!"),  # Большой индекс
        (
            "1 2\n-1",
            "2",  # Отрицательный индекс
        ),
    ],
)
def test_11_3_5(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_11_3_5()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        # Sample Input 1: ключ "height" отсутствует
        (
            '{"name": "Arthur", "age": 30}\nheight',
            "Запрашиваемый ключ height отсутствует у словаря!",
        ),
        # Sample Input 2: ключ "age" существует
        (
            '{"animal": "dog", "color": "brown", "age": 3}\nage',
            "3",
        ),
        # Дополнительные случаи
        (
            '{"a": 1, "b": 2}\nc',
            "Запрашиваемый ключ c отсутствует у словаря!",
        ),
        (
            '{"test": "value"}\ntest',
            "value",
        ),
        (
            "{} \nkey",
            "Запрашиваемый ключ key отсутствует у словаря!",
        ),
        (
            '{"num": 42}\n42',
            "Запрашиваемый ключ 42 отсутствует у словаря!",
        ),
        (
            '{"true": "yes"}\nfalse',
            "Запрашиваемый ключ false отсутствует у словаря!",
        ),
    ],
)
def test_11_3_6(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_11_3_6()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        # Sample Input 1: "3,14" → заменить , на . → float → int = 3
        ("3,14", "3"),
        # Sample Input 2: "123" → int() сразу работает
        ("123", "123"),
        # Дополнительные случаи
        ("5,67", "5"),  # 5.67 → 5
        ("-2,34", "-2"),  # -2.34 → -2
        ("0,99", "0"),  # 0.99 → 0
        ("42", "42"),  # Целое без запятой
        ("10,0", "10"),  # 10.0 → 10
    ],
)
def test_11_3_7(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_11_3_7()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
