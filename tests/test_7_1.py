import pytest
from src.module_7 import (
    m_7_1_1,
    m_7_1_2,
    m_7_1_3,
    m_7_1_4,
)


def test_7_1_1(mocker, capsys):
    mocker.patch("builtins.input", side_effect=["hello world python"])
    m_7_1_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == "['hello', 'world', 'python']"


def test_7_1_2(capsys):
    m_7_1_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == "[1, 2, 3, 4, 5, 6]"


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3 4", "[1, 2, 3, 4]"),
        ("-1 0 1", "[-1, 0, 1]"),
        ("5", "[5]"),
        ("10 20 30 40 50", "[10, 20, 30, 40, 50]"),
    ],
)
def test_7_1_3(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=[input_data])
    m_7_1_3()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3 4", "10"),
        ("5 10 15", "30"),
        ("-1 1 -1", "-1"),
        ("100", "100"),
    ],
)
def test_7_1_4(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=[input_data])
    m_7_1_4()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
