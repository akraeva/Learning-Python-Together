import pytest
from src.module_10 import (
    m_10_5_1,
    m_10_5_2,
)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Arthur", "84.0"),
        ("Alice", "88.0"),
        ("Anna", "91.2"),
        ("Vsevolod", "Студент Vsevolod в словаре не найден"),
        ("Elena", "88.4"),
    ],
)
def test_10_5_1(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_10_5_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("Arthur\nage", "21"),
        ("Vsevolod\nage", "Запрашиваемый студент Vsevolod не найден"),
        ("Anna\nheight", "Запрашиваемый параметр height у студента Anna не найден"),
        ("Alice\nmajor", "Computer Science"),
        ("Stepan\ngrades", "[85, 88, 90, 92, 89]"),
    ],
)
def test_10_5_2(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_10_5_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
