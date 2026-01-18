import pytest
from src.module_9 import (
    m_9_5_1,
    m_9_5_2,
    m_9_5_3,
    m_9_5_4,
    m_9_5_5,
    m_9_5_6,
    m_9_5_7,
    m_9_5_8,
    m_9_5_9,
    m_9_5_10,
    m_9_5_11,
    m_9_5_12,
    m_9_5_13,
    m_9_5_14,
    m_9_5_15,
)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 2 3", "1\n2\n3"),
        ("5 5 5", "5"),
        ("1 3 2 4 2", "1\n2\n3\n4"),
        ("-1 0 1", "-1\n0\n1"),
    ],
)
def test_9_5_01(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=[input_data])
    m_9_5_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("abcde", "5"),
        ("aabbcc", "3"),
        ("hello", "4"),
        ("aaaa", "1"),
    ],
)
def test_9_5_2(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=[input_data])
    m_9_5_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("banana", "a, b, n"),
        ("hello", "e, h, l, o"),
        ("aabbcc", "a, b, c"),
        ("xyz", "x, y, z"),
    ],
)
def test_9_5_3(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=[input_data])

    m_9_5_3()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3\n3 4 5", "[1, 2, 3, 4, 5]"),
        ("1 1\n2 2", "[1, 2]"),
        ("-1 0\n0 1", "[-1, 0, 1]"),
        ("5\n5", "[5]"),
    ],
)
def test_9_5_4(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_9_5_4()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3\n2 3 4", "[2, 3]"),
        ("1 2\n2 3", "[2]"),
        ("1 2 3\n4 5", "[]"),
        ("1 1\n1 1", "[1]"),
    ],
)
def test_9_5_5(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_9_5_5()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3\n2 3", "[1]"),
        ("4 5 6\n1 2", "[4, 5, 6]"),
        ("1 2 3\n4 5 6", "[1, 2, 3]"),
        ("1 1\n2", "[1]"),
    ],
)
def test_9_5_6(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_9_5_6()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2\n2 3", "[1, 3]"),
        ("1 2 3\n3 4", "[1, 2, 4]"),
        ("1 2\n3 4", "[1, 2, 3, 4]"),
        ("1\n1", "[]"),
    ],
)
def test_9_5_7(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_9_5_7()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2\n2 3\n4", "[2, 4]"),
        ("1 2 3\n2 3 4\n5", "[2, 3, 5]"),
        ("1\n1\n1", "[1]"),
        ("1 2\n3\n2 3", "[2, 3]"),
    ],
)
def test_9_5_8(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_9_5_8()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("123", "True"),
        ("112", "False"),
        ("9876543210", "True"),
        ("111", "False"),
    ],
)
def test_9_5_9(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=[input_data])
    m_9_5_9()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3\n3 2 1", "True"),
        ("1 2\n1 3", "False"),
        ("5\n5", "True"),
        ("1 2 3\n4", "False"),
    ],
)
def test_9_5_10(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_9_5_10()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3\n3", "[1, 2, 3]"),
        ("1 1\n2", "[1, 2]"),
        ("1 2\n1", "[1, 2]"),
        ("5\n5", "[5]"),
    ],
)
def test_9_5_11(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_9_5_11()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3\n4", "[1, 2, 3]"),
        ("1 2\n1", "[2]"),
        ("5\n6", "[5]"),
        ("1 1\n1", "[]"),
    ],
)
def test_9_5_12(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_9_5_12()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2\n1 2 3", "True"),
        ("1 3\n1 2", "False"),
        ("1\n1 2", "True"),
        ("2\n1", "False"),
    ],
)
def test_9_5_13(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_9_5_13()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3\n1 2", "True"),
        ("1 2\n1 2 3", "False"),
        ("1 2\n1", "True"),
        ("1\n2", "False"),
    ],
)
def test_9_5_14(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_9_5_14()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("123\n321", "True"),
        ("123\n124", "False"),
        ("111\n111", "True"),
        ("12\n21", "True"),
    ],
)
def test_9_5_15(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_9_5_15()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
