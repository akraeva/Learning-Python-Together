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
            "['metallica']\n['dragons', 'imagine']\n['pink', 'queen']",
        ),
        ("a b c\nd e f", "[]\n['a', 'b', 'c']\n['d', 'e', 'f']"),
        ("rock\nrock metal", "['rock']\n[]\n['metal']"),
        ("a b c\na b c", "['a', 'b', 'c']\n[]\n[]"),
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
        (
            "Аэрофотосъёмка ландшафта уже выявила земли богачей и процветающих крестьян.",
            "True",
        ),
        ("Съешь же ещё этих мягких французских булок, да выпей чаю", "True"),
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
            "Arthur Peter Anna Alice Anastasia"
            "\nAlice Arthur Vasily Anastasia Anna Tatiana Victoria Vadim",
            "Alice, Anastasia, Anna, Arthur\n"
            "Peter\n"
            "Tatiana, Vadim, Vasily, Victoria\n"
            "Peter, Tatiana, Vadim, Vasily, Victoria",
        ),
        (
            "ivan petya\npetya katya",
            "petya\nivan\nkatya\nivan, katya",
        ),
        ("a b c\nd e", "-\na, b, c\nd, e\na, b, c, d, e"),
        ("x\nx y z", "x\n-\ny, z\ny, z"),
        ("1\n2", "-\n1\n2\n1, 2"),
    ],
)
def test_9_6_5(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_9_6_5()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
