import pytest
from src.module_7 import (
    m_7_2_1,
    m_7_2_2,
)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("2\nhello world python", "python"),
        ("0\nabc def ghi", "abc"),
        ("1\na b c d", "b"),
        ("4\n1 2 3 4 5", "5"),
    ],
)
def test_7_2_1(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_7_2_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2\nhello world python", "['world']"),
        ("0 2\na b c d", "['a', 'b']"),
        ("2 5\n1 2 3 4 5 6", "['3', '4', '5']"),
        ("0 1\nx", "['x']"),
    ],
)
def test_7_2_2(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_7_2_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
