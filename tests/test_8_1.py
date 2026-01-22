import pytest
from src.module_8 import (
    m_8_1_1,
    m_8_1_2,
)


def test_8_1_1(capsys):
    m_8_1_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == "(1, 2, 3, 4, 5)\n<class 'tuple'>"


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3\n10", "(10, 2, 3)"),  # x=10
        ("5 6\n99", "(99, 6)"),  # x=99
        ("-1 0\n42", "(42, 0)"),  # x=42
        ("7\n100", "(100,)"),  # single element
    ],
)
def test_8_1_2(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_8_1_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
