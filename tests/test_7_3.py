import pytest
from src.module_7 import (
    m_7_3_1,
    m_7_3_2,
    m_7_3_3,
)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3\n4 5", "[1, 2, 3, 4, 5]"),
        ("10\n20 30", "[10, 20, 30]"),
        ("-1 0\n1", "[-1, 0, 1]"),
        ("5 6 7\n8 9 10", "[5, 6, 7, 8, 9, 10]"),
    ],
)
def test_7_3_1(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_7_3_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2\n3", "[1, 2, 1, 2, 1, 2]"),
        ("10\n0", "[]"),
        ("5 6\n2", "[5, 6, 5, 6]"),
        ("1 2\n1", "[1, 2]"),
    ],
)
def test_7_3_2(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_7_3_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3\n10", "[1, 2, 3, 10]"),
        ("5 6\n99", "[5, 6, 99]"),
        ("-1 0 1\n42", "[-1, 0, 1, 42]"),
        ("1 1\n1", "[1, 1, 1]"),
    ],
)
def test_7_3_3(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_7_3_3()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
