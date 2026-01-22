import pytest
from src.module_8 import (
    m_8_3_1,
    m_8_3_2,
)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3 4\n2", "1"),  # index of 2
        ("5 5 5\n5", "0"),  # first occurrence
        ("1 3 5\n2", "Искомый элемент не найден"),
        ("1 10 1000\n100", "Искомый элемент не найден"),
    ],
)
def test_8_3_1(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_8_3_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 5 3 4 2", "1"),  # max=5 at index 1
        ("7 1 9 2", "2"),  # max=9 at index 2
        ("5 5 5", "0"),  # first max
        ("-1 -5 -2", "0"),  # max=-1 at index 0
    ],
)
def test_8_3_2(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=[input_data])
    m_8_3_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
