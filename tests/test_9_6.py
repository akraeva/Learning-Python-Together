import pytest
from src.module_9 import (
    m_9_6_1,
    m_9_6_2,
    m_9_6_3,
    m_9_6_4,
    m_9_6_5,
)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            "Проверим! На сколько пройдёт? Мало ли; Не учли чего: "
            "пропустили чего. Момент - который с тире там...",
            "который\nли\nмало\nмомент\nна\nне\nпроверим\n"
            "пройдёт\nпропустили\nс\nсколько\nтам\nтире\nучли\nчего",
        ),
        ("Hello, world!", "hello\nworld"),
        ("Привет - мир! Как?", "как\nмир\nпривет"),
        ("a. b .c", "a\nb\nc"),
        ("test - case.", "case\ntest"),
    ],
)
def test_9_6_1(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=[input_data])
    m_9_6_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            "imagine dragons metallica\nmetallica queen pink",
            "common: metallica\nvasya: dragons imagine\npetya: pink queen",
        ),
        ("a b c\nd e f", "common: -\nvasya: a b c\npetya: d e f"),
        ("rock\nrock metal", "common: rock\nvasya: -\npetya: metal"),
        ("abc\nabc", "common: a b c\nvasya: -\npetya: -"),
    ],
)
def test_9_6_2(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_9_6_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Съешь же ещё этих мягких французских булок", "True"),
        ("привет мир", "False"),
        ("абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "True"),
        ("а б в", "False"),
    ],
)
def test_9_6_3(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=[input_data])
    m_9_6_3()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("3\ncat\ntac\nact", "True"),
        ("2\nab\nabc", "False"),
        ("4\nstop\npots\ntops\npost", "True"),
        ("1\na", "True"),
    ],
)
def test_9_6_4(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_9_6_4()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            "ivan petya\npetya katya",
            "both: petya\ninform: ivan\nphysic: katya\none: ivan katya petya",
        ),
        ("a b c\nd e", "both: -\ninform: a b c\nphysic: d e\none: a b c d e"),
        ("x\nx y z", "both: x\ninform: -\nphysic: y z\none: x y z"),
        ("1\n2", "both: -\ninform: 1\nphysic: 2\none: 1 2"),
    ],
)
def test_9_6_5(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_9_6_5()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
