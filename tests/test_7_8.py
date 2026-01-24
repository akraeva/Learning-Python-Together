import pytest
from src.module_7 import (
    m_7_8_1,
    m_7_8_2,
    m_7_8_3,
    m_7_8_4,
)


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("2\n1 2 3\n4 5 6", "[[1, 2, 3], [4, 5, 6]]"),
        ("1\n7 8", "[[7, 8]]"),
        ("3\n1\n2 3\n4 5 6", "[[1], [2, 3], [4, 5, 6]]"),
        ("2\n-1 -2\n0 0", "[[-1, -2], [0, 0]]"),
    ],
)
def test_7_8_1(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_7_8_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("2\n1 2 3\n4 5 6\n5", "1 1"),  # matrix[1][1] == 5
        ("3\n1 2\n3 4\n5 6\n6", "2 1"),
        ("1\n10 20 30\n40", "Элемент 40 не найден!"),
        ("2\n-1 -2\n0 1\n-2", "0 1"),
    ],
)
def test_7_8_2(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_7_8_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("2\n1 2 3\n4 5 6", "[5, 7, 9]"),
        ("1\n10 20 30", "[10, 20, 30]"),
        ("3\n1\n2\n3", "[6]"),
        ("2\n-1 -2\n3 4", "[2, 2]"),
    ],
)
def test_7_8_3(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_7_8_3()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("2\n1 2 3\n4 5 6", "1 4\n2 5\n3 6"),
        ("1\n7 8 9", "7\n8\n9"),
        ("3\n1\n2\n3", "1 2 3"),
        ("2\n-1 -2\n3 4", "-1 3\n-2 4"),
    ],
)
def test_7_8_4(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_7_8_4()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
