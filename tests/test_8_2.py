import pytest
from src.module_8 import (
    m_8_2_1,
    m_8_2_2,
    m_8_2_3,
)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2\n3 4", "(1, 2, 3, 4)"),
        ("5\n", "(5,)"),
        ("-1 0 1\n2 -2", "(-1, 0, 1, 2, -2)"),
        ("97 98\n99 100", "(97, 98, 99, 100)"),
    ],
)
def test_8_2_1(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_8_2_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2\n3", "(1, 2, 1, 2, 1, 2)"),  # n=3
        ("97\n2", "(97, 97)"),  # n=2
        ("1\n0", "()"),  # n=0
        ("5 6 7\n1", "(5, 6, 7)"),
    ],
)
def test_8_2_2(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_8_2_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3\n10", "(1, 2, 3, 10)"),
        ("5\n99", "(5, 99)"),
        ("-1 0\n42", "(-1, 0, 42)"),
        ("97\n1", "(97, 1)"),
    ],
)
def test_8_2_3(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_8_2_3()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
