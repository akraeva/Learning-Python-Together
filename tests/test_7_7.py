import pytest
from src.module_7 import (
    m_7_7_1,
    m_7_7_2,
    m_7_7_3,
    m_7_7_4,
    m_7_7_5,
    m_7_7_6,
)


# === 7.7 Списковые включения ===


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 5", "[1, 4, 9, 16]"),
        ("0 4", "[0, 1, 4, 9]"),
        ("-2 3", "[4, 1, 0, 1, 4]"),
        ("2 3", "[4]"),
    ],
)
def test_7_7_1(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_7_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 8", "[2, 4, 6]"),
        ("0 7", "[0, 2, 4, 6]"),
        ("-3 4", "[-2, 0, 2]"),
        ("2 3", "[2]"),
    ],
)
def test_7_7_2(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_7_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3 4 5", "[2, 4]"),
        ("-2 -1 0 1 2", "[-2, 0, 2]"),
        ("1 3 5", "[]"),
        ("2", "[2]"),
    ],
)
def test_7_7_3(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_7_3()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3 4 5", "2"),
        ("-2 -1 0 1 2", "3"),
        ("1 3 5", "0"),
        ("2", "1"),
    ],
)
def test_7_7_4(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_7_4()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("a bb ccc", "[1, 2, 3]"),
        ("слово два три", "[5, 3, 3]"),
        ("one", "[3]"),
        ("aa aaa aaaa", "[2, 3, 4]"),
    ],
)
def test_7_7_5(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_7_5()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("50 101 102 103", "[102, 102, 104]"),
        ("99 100 200", "[200]"),
        ("101", "[102]"),
        ("150 151", "[150, 152]"),
    ],
)
def test_7_7_6(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_7_6()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
