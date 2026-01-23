import pytest
from src.module_10 import (
    m_10_2_1,
    m_10_2_2,
    m_10_2_3,
    m_10_2_4,
    m_10_2_5,
)


def test_10_2_1(capsys):
    m_10_2_1()
    captured = capsys.readouterr()
    expected = "{'name': 'Иван', 'surname': 'Иванов', 'age': 25}"
    assert captured.out.strip() == expected


def test_10_2_2(capsys):
    m_10_2_2()
    captured = capsys.readouterr()
    expected = (
        "{1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}"
    )
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        ("Иван\nИванов\nname", "Иван"),
        ("Анна\nПетрова\nsurname", "Петрова"),
    ],
)
def test_10_2_3(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_10_2_3()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("15.03.2024", "15 марта 2024 года"),
        ("03.13.2024", "Указанного месяца в дате не существует!"),
        ("25.12.1999", "25 декабря 1999 года"),
    ],
)
def test_10_2_4(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=[input_data])
    m_10_2_4()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (
            "Иван Анна\n+79123456789 +79876543210\n2\nИван\nАнна",
            "+79123456789\n+79876543210",
        ),
        (
            "Петр Мария\n+79991234567 +79997654321\n3\nПетр\nМария\nСидор",
            "+79991234567\n+79997654321\nНе найдено",
        ),
    ],
)
def test_10_2_5(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_10_2_5()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
