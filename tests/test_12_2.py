import pytest
from src.module_12 import (
    m_12_2_1,
    m_12_2_2,
    m_12_2_3,
    m_12_2_4,
    m_12_2_5,
    m_12_2_6,
    m_12_2_7,
    m_12_2_8,
    m_12_2_9,
    m_12_2_10,
    m_12_2_11,
    m_12_2_12,
    m_12_2_13,
    m_12_2_14,
    m_12_2_15,
    m_12_2_16,
)


def test_12_2_1(capfd):
    """Тест greet() без параметров -> 'Hello, world!'"""
    m_12_2_1()
    captured = capfd.readouterr()
    assert captured.out.strip() == "Hello, world!"


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Alice", "Hello, Alice!"),
        ("Боб", "Hello, Боб!"),
        ("123", "Hello, 123!"),
        ("", "Hello, !"),
    ],
)
def test_12_2_2(self, capfd, name, expected):
    """Тест greet(name) с параметром"""
    m_12_2_2()
    captured = capfd.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "args, expected",
    [
        # Без аргументов (default "unknown")
        ([], "Hello, unknown!"),
        # С аргументами
        (["Alice"], "Hello, Alice!"),
        (["Боб"], "Hello, Боб!"),
        ([""], "Hello, !"),
    ],
)
def test_m_12_2_3(self, capfd, args, expected):
    """Тест greet(name='unknown') с параметром по умолчанию"""
    m_12_2_3.greet(*args)
    captured = capfd.readouterr()
    assert captured.out.strip() == expected
