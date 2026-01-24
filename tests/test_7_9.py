import pytest
from src.module_7 import (
    m_7_9_1,
    m_7_9_2,
    m_7_9_3,
    m_7_9_4,
    m_7_9_5,
    m_7_9_6,
    m_7_9_7,
    m_7_9_8,
    m_7_9_9,
    m_7_9_10,
    m_7_9_11,
    m_7_9_12,
)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3 4 5", "[5, 2, 3, 4, 1]"),
        ("10 5 7", "[5, 10, 7]"),
        ("-1 0 1", "[1, 0, -1]"),
        ("2 1", "[1, 2]"),
    ],
)
def test_7_9_1(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_9_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3 4 5", "3"),
        ("10 20 30", "10"),
        ("-1 0 1 2", "0"),
        ("5 1 3 2 4", "3"),
    ],
)
def test_7_9_2(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_9_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("1 2 3 2 4 2\n2", "[1, 3, 4]"),
        ("5 5 5\n5", "[]"),
        ("1 2 3\n4", "Элемент 4 не обнаружен"),
        ("1 1 2 1 3\n1", "[2, 3]"),
    ],
)
def test_7_9_3(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_7_9_3()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3 2 1 3 3", "3"),
        ("5 5 5 1 2", "5"),
        ("1 2 3 4", "1"),  # при одинаковой частоте берётся первый
        ("-1 -1 0 0 0", "0"),
    ],
)
def test_7_9_4(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_9_4()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("2 99\n1 2 3 4", "[1, 99, 3, 4]"),
        ("5 0\n1 2 3 4", "[1, 2, 3, 4]"),  # нет 5 — список без изменений
        ("1 10\n1", "[10]"),
        ("3 7\n3 3 3", "[7, 3, 3]"),  # заменяется только первое вхождение
    ],
)
def test_7_9_5(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_7_9_5()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("абвa бaва", "True"),  # анаграммы
        ("listen silent", "True"),
        ("abc abd", "False"),
        ("ааа аа", "False"),
    ],
)
def test_7_9_6(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_9_6()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3 2 4 5", "2\n3\n4\n5"),
        ("5 4 3 2 1", ""),  # всегда убывает — ничего не выводим
        ("1 1 1 2", "2"),
        ("-1 0 1", "0\n1"),
    ],
)
def test_7_9_7(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_9_7()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("ab", "[['a', 97], ['b', 98]]"),
        ("A*", "[['A', 65], ['*', 42]]"),
        ("я", "[['я', 1103]]"),
        ("12", "[['1', 49], ['2', 50]]"),
    ],
)
def test_7_9_8(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_9_8()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (
            "193 192 185 183 180 180 177 176 176 174 172 172 171 171 168 167\n183",
            "4",
        ),
        ("165 163 160 157 150\n149", "6"),
        ("165 163 160 157 150\n170", "1"),
        ("199 190 180 170\n185", "3"),
        ("200 190 180 180 170\n180", "3"),
        ("180\n175", "2"),
    ],
)
def test_7_9_9(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_7_9_9()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3", "2"),
        ("3 1 2", "2"),
        ("1 2 3 4", "2.5"),
        ("7 7 7 7", "7.0"),
    ],
)
def test_7_9_10(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_9_10()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (
            "4 4\n- - - - -\n- * - - -\n- - - - -\n- - - * -\n- - - - -",
            "Есть пробитие",
        ),
        (
            "1 1\n* - - - -\n- - - - -\n- - - - -\n- - - - -\n- - - - -",
            "Есть пробитие",
        ),
        (
            "5 2\n- - - - -\n- - - - -\n- - - - -\n- - - - -\n- - - - -",
            "Мимо",
        ),
        (
            "2 4\n- - - - -\n- - - - -\n- - * - -\n- - - - -\n- - - - *",
            "Мимо",
        ),
    ],
)
def test_7_9_11(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_7_9_11()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("5 3 2 8 1 4", "[1, 3, 2, 8, 5, 4]"),  # нечётные отсортированы: 1,3,5
        ("2 4 6", "[2, 4, 6]"),  # только чётные — без изменений
        ("1 3 5", "[1, 3, 5]"),  # нечётные уже отсортированы
        ("9 8 7 6 5", "[5, 8, 7, 6, 9]"),
    ],
)
def test_7_9_12(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_9_12()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
