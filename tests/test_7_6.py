import pytest
from src.module_7 import (
    m_7_6_1,
    m_7_6_2,
    m_7_6_3,
    m_7_6_4,
    m_7_6_5,
    m_7_6_6,
    m_7_6_7,
    m_7_6_8,
    m_7_6_9,
    m_7_6_10,
    m_7_6_11,
    m_7_6_12,
    m_7_6_13,
    m_7_6_14,
    m_7_6_15,
    m_7_6_16,
)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3 4", "[4, 2, 3, 1]"),
        ("5", "[5]"),  # single element
        ("10 20 30 40 50", "[50, 20, 30, 40, 10]"),
    ],
)
def test_7_6_1(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_6_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3", "6"),
        ("-1 1 -1", "-1"),
        ("10", "10"),
    ],
)
def test_7_6_2(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_6_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 3 4 5", "5"),
        ("10", "1"),
        ("-5 0 5", "3"),
    ],
)
def test_7_6_3(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_6_3()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("3 1 4 1 5", "1 5"),
        ("10 20 30", "10 30"),
        ("5", "5 5"),
    ],
)
def test_7_6_4(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_6_4()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("2 4 6", "4.0"),
        ("1 3 5 7", "4.0"),
        ("10 20", "15.0"),
    ],
)
def test_7_6_5(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_6_5()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("-1 2 -3 4 0", "2"),
        ("1 2 3", "3"),
        ("-5 -4 -3", "0"),
    ],
)
def test_7_6_6(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_6_6()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("a bb ccc d", "a ccc"),
        ("hi hello world", "hi hello"),
        ("a", "a a"),
    ],
)
def test_7_6_7(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_6_7()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("5 3 8 1 4", "[1, 3, 4, 5, 8]\n[8, 5, 4, 3, 1]"),
        ("10 20 10", "[10, 10, 20]\n[20, 10, 10]"),
        ("1", "[1]\n[1]"),
    ],
)
def test_7_6_8(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data.split("\n")[0])
    m_7_6_8()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected.strip()


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1 2 2 3 3 3 4", "[1, 2, 3, 4]"),
        ("5 5 5", "[5]"),
        ("1 2 3 4 5", "[1, 2, 3, 4, 5]"),
    ],
)
def test_7_6_9(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_6_9()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("-5 3 -1 0 4", "[0, -1, 3, 4, -5]"),
        ("10 -20 5", "[5, 10, -20]"),
        ("1 1 1", "[1, 1, 1]"),
    ],
)
def test_7_6_10(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_7_6_10()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("1 2 3 4\n2", "[1, 3, 4]"),
        ("5 5 5\n10", "Элемент 10 не обнаружен"),
        ("1 2 3\n3", "[1, 2]"),
    ],
)
def test_7_6_11(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_7_6_11()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("1 2 3 4\n2", "1"),
        ("5 5 5\n10", "Элемент 10 не обнаружен"),
        ("1 2 3 0\n0", "3"),
    ],
)
def test_7_6_12(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_7_6_12()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("1 2 2 3 2\n2", "3"),
        ("5 5 5\n5", "3"),
        ("1 2 3\n10", "0"),
    ],
)
def test_7_6_13(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_7_6_13()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("1 2 3\n10", "[1, 2, 3, 10]"),
        ("5\n20", "[5, 20]"),
        ("\n100", "[100]"),
    ],
)
def test_7_6_14(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_7_6_14()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("1 2 3\n4 5 6", "[1, 2, 3, 4, 5, 6]"),
        ("10\n20 30", "[10, 20, 30]"),
        ("1 2\n3", "[1, 2, 3]"),
    ],
)
def test_7_6_15(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_7_6_15()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("1 2 3\n10\n1", "[1, 10, 2, 3]"),
        ("5\n20\n0", "[20, 5]"),
        ("97 98 99\n99\n2", "[97, 98, 99, 99]"),
    ],
)
def test_7_6_16(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_7_6_16()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
