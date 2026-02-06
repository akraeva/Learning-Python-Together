import pytest
from src.module_12 import (
    m_12_7_1,
    m_12_7_2,
    m_12_7_3,
    m_12_7_4,
    m_12_7_5,
    m_12_7_6,
    m_12_7_7,
)


# m_12_7_1: Анонимная функция
@pytest.mark.parametrize(
    "num, expected",
    [
        (3, 6),  # Sample Input
        (0, 0),  # Ноль
        (1, 2),  # Единица
        (-5, -10),  # Отрицательное
        (10, 20),  # Большее число
    ],
)
def test_12_7_1(num, expected):
    result = m_12_7_1(num)
    assert result == expected


# m_12_7_2: Выводим определённые слова (избранные) из списка
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("эта актёрка явно амёбная", "актёрка амёбная"),  # Sample 1
        ("несколько слов из моего списка слов", "Нет"),  # Sample 2
        ("", "Нет"),  # Пустой ввод
        ("кот котик котёнок", "котёнок"),  # Одно слово 7 букв
        ("hello worls конфета candy привет мир ", "конфета"),  # Смешанный алфавит
    ],
)
def test_12_7_2(input_str, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_str)
    m_12_7_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


# m_12_7_3: Работаем со списком чисел
@pytest.mark.parametrize(
    "input_str, expected",
    [
        ("10 20 30 40 50 60 70 80 90", "5 10 15 20"),  # Sample 1
        ("50 51", "Нет"),  # Sample 2
        ("", "Нет"),  # Пустой ввод
        ("2 47 3 48 4", "1 2"),  # Граница 47, четность
        ("1 3 5 7 9", "Нет"),  # Только нечетные
    ],
)
def test_12_7_3(input_str, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_str)
    m_12_7_3()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


# m_12_7_4: Фильтрация словаря
@pytest.mark.parametrize(
    "input_json, expected",
    [
        (
            '{"Arthur": 60, "Vladimir": 75, "Anna": 85, "Alice": 95, "Brian": 80}',
            "{'Anna': 85, 'Alice': 95}",
        ),  # Sample
        ('{"Max": 81, "Eva": 80}', "{'Max': 81}"),  # Граница >80
        ("{}", "{}"),  # Пустой словарь
        ('{"Ivan": 90, "Oleg": 70}', "{'Ivan': 90}"),  # Одно совпадение
        (
            '{"bad": 50, "good": 100, "border": 80}',
            "{'good': 100}",
        ),  # Несколько, граница
    ],
)
def test_12_7_4(input_json, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_json)
    m_12_7_4()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


# m_12_7_5: Сортируем список
@pytest.mark.parametrize(
    "input_str, expected",
    [
        (
            "яблоко ананас мандарин груша вишня слива абрикос персик манго",
            "вишня груша манго слива ананас персик яблоко абрикос мандарин",
        ),  # Sample
        ("кот собака петух", "кот петух собака"),  # 3-5-5 → кот(3), собака(5), петух(5)
        ("a bb ccc dddd", "a bb ccc dddd"),  # Английский алфавит
        ("", ""),  # Пустой список
        ("aaa bbb ccc", "aaa bbb ccc"),  # Равные длины
    ],
)
def test_12_7_5(input_str, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_str)
    m_12_7_5()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


# m_12_7_6: По убыванию оценок станооовись
@pytest.mark.parametrize(
    "input_json, expected",
    [
        (
            '{"Alice": 90, "Arthur": 85, "Vladimir": 85, "Brian": 85}',
            "Alice - 90\nArthur - 85\nVladimir - 85\nBrian - 85",
        ),  # Sample
        (
            '{"Max": 100, "Eva": 90, "Tom": 80}',
            "Max - 100\nEva - 90\nTom - 80",
        ),  # Убывание
        ('{"A": 50}', "A - 50"),  # Один студент
        ("{}", ""),  # Пустой словарь
        (
            '{"first": 95, "second": 100, "third": 95}',
            "second - 100\nfirst - 95\nthird - 95",
        ),  # Равные оценки
    ],
)
def test_12_7_6(input_json, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_json)
    m_12_7_6()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected.strip()


# m_12_7_7: По убыванию оценок станооовись 2
@pytest.mark.parametrize(
    "input_json, expected",
    [
        (
            '{"Alice": 90, "Arthur": 85, "Vladimir": 85, "Brian": 85}',
            "Alice - 90\nArthur - 85\nBrian - 85\nVladimir - 85",
        ),  # Sample
        (
            '{"Zoe": 90, "Amy": 90, "Bob": 85}',
            "Amy - 90\nZoe - 90\nBob - 85",
        ),  # 90: Amy < Zoe лексикографически
        ('{"Max": 100}', "Max - 100"),  # Один студент
        ("{}", ""),  # Пустой словарь
        (
            '{"Eve": 95, "Dan": 95, "Ann": 100, "Bob": 95}',
            "Ann - 100\nBob - 95\nDan - 95\nEve - 95",
        ),  # Сложная сортировка
    ],
)
def test_12_7_7(input_json, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_json)
    m_12_7_7()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected.strip()
