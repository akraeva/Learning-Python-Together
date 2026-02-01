import pytest
from src.module_10 import (
    m_10_7_1,
    m_10_7_2,
    m_10_7_3,
    m_10_7_4,
    m_10_7_5,
    m_10_7_6,
    m_10_7_7,
    m_10_7_8,
)


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (
            '{"яблоки": 10, "бананы": 5, "апельсины": 15}\n{"яблоки": 5, "киви": 8, "апельсины": 10}',
            "апельсины - 25\nбананы - 5\nкиви - 8\nяблоки - 15",
        ),
        (
            '{"a": 1, "b": 2}\n{"b": 3, "c": 4}',
            "a - 1\nb - 5\nc - 4",
        ),
        (
            '{"x": 10}\n{}',
            "x - 10",
        ),
        (
            '{}\n{"y": 20}',
            "y - 20",
        ),
        (
            '{"cat": 1, "dog": 2, "rat": 3}\n{"dog": 5, "rat": 1, "bat": 4}',
            "bat - 4\ncat - 1\ndog - 7\nrat - 4",
        ),
    ],
)
def test_10_7_1(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_10_7_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        # Sample 1: encode
        ("encode\nHello", ".... . .-.. .-.. ---"),
        # Sample 2: decode
        ("decode\n. -.. ..- -.-. .- - .. --- -.", "Education"),
        # Дополнительно: encode
        ("encode\nPython", ".--. -.-- - .... --- -."),
        ("encode\nSOS", "... --- ..."),
        ("encode\n42", "....- ..---"),
        # Дополнительно: decode
        ("decode\n....- ..---", "42"),
        ("decode\n... --- ...", "Sos"),
        ("decode\n.--. -.-- - .... --- -.", "Python"),
        ("decode\n.... . .-.. .-.. ---", "Hello"),
    ],
)
def test_10_7_2(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_10_7_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        # Sample Input
        (
            "5\nРоссия: Москва\nТурция: Стамбул\nИталия: Милано\nРоссия: Санкт-Петербург\nИталия: Палермо",
            """Италия:
Милано
Палермо
Россия:
Москва
Санкт-Петербург
Турция:
Стамбул""",
        ),
        # Один город на страну
        (
            "3\nФранция: Париж\nГермания: Берлин\nИспания: Мадрид",
            """Германия:
Берлин
Испания:
Мадрид
Франция:
Париж""",
        ),
        # Повторяющиеся города (должны остаться один раз)
        (
            "4\nUSA: New York\nUSA: Los Angeles\nUSA: New York\nCanada: Toronto",
            """Canada:
Toronto
USA:
Los Angeles
New York""",
        ),
        # Одна страна, несколько городов
        (
            "4\nJapan: Tokyo\nJapan: Kyoto\nJapan: Osaka\nJapan: Tokyo",
            """Japan:
Kyoto
Osaka
Tokyo""",
        ),
        # Минимум данных
        (
            "1\nPoland: Warsaw",
            """Poland:
Warsaw""",
        ),
    ],
)
def test_10_7_3(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_10_7_3()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected.strip()


@pytest.mark.parametrize(
    "inputs, expected",
    [
        # Sample Input
        (
            '{"др.": "других", "пр.": "прочие"}\nИ пр. методы др. исполнителей',
            "И прочие методы других исполнителей",
        ),
        # Простая замена
        (
            '{"к.": "который", "н.": "наш"}\nк. н. дом',
            "Который наш дом",
        ),
        # Несколько замен в одном слове (не должно заменять частично)
        (
            '{"т.": "так", "к.": "как"}\nТ. к. очень хорошо',
            "Так как очень хорошо",  # "т.к." нет в словаре → остаётся
        ),
        # Нет сокращений в тексте
        (
            '{"abc": "test"}\nОбычный текст без сокращений',
            "Обычный текст без сокращений",  # замена не происходит
        ),
        # Пустой словарь
        (
            "{} \nПривет мир!",
            "Привет мир!",  # словарь пустой → текст без изменений
        ),
    ],
)
def test_10_7_4(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_10_7_4()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        # Sample Input
        (
            """3
python.exe R
book.txt R W
notebook.exe R W X
5
execute python.exe
read book.txt
write notebook.exe
execute notebook.exe
write book.txt""",
            "Access denied\nOK\nOK\nOK\nOK",
        ),
        # Только чтение
        (
            """2
file1.txt R
file2.exe X
3
read file1.txt
execute file1.txt
read file2.exe""",
            "OK\nAccess denied\nAccess denied",
        ),
        # Все права
        (
            """1
full.txt R W X
3
read full.txt
write full.txt
execute full.txt""",
            "OK\nOK\nOK",
        ),
        # Нет прав на запись
        (
            """2
doc.pdf R
app.exe R X
2
write doc.pdf
write app.exe""",
            "Access denied\nAccess denied",
        ),
        # Минимальный тест
        (
            """1
test R
1
read test""",
            "OK",
        ),
    ],
)
def test_10_7_5(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_10_7_5()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected.strip()


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("5 3 4 7 7 5 5 5", "426"),
        ("1 1 1 1 1 1 1 1 1 1", "120"),
        ("1 10 1 10 1 10 1 10", "456"),
        ("1 2 3 4 5 6 7 8 9", "468"),
        ("42", "422"),
    ],
)
def test_10_7_6(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_10_7_6()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected.strip()


@pytest.mark.parametrize(
    "inputs, expected",
    [
        # Sample Input
        (
            '{"Паста карбонара": 450, "Салат Цезарь": 400, "Стейк лосося": 600, "Пицца Маргарита": 550, "Бургер с картофелем фри": 500, "Фриттата с овощами": 350, "Тирамису": 300, "Чёрный чай": 70, "Зелёный чай": 80, "Кофе Американо": 200, "Кофе Капучино": 300, "Кофе Латте": 350}\n4\nПаста карбонара - 1\nСалат Цезарь - 2\nЧёрный чай - 2\nКофе Капучино - 1',
            "1690",
        ),
        # Один заказ
        (
            '{"burger": 500}\n1\nburger - 2',
            "1000",
        ),
        # Дорогие блюда
        (
            '{"steak": 1000, "wine": 500}\n2\nsteak - 1\nwine - 2',
            "2000",
        ),
        # Дешёвые + количество
        (
            '{"tea": 50, "coffee": 100}\n3\ntea - 3\ncoffee - 1\ntea - 2',
            "350",
        ),
        # Максимальное количество
        (
            '{"pizza": 550}\n1\npizza - 10',
            "5500",
        ),
    ],
)
def test_10_7_7(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_10_7_7()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        # Sample Input
        (
            """5
Максим Тетрадь 4
Николай Карандаш 3
Максим Ручка 1
Ирина Линейка 4
Максим Тетрадь 2""",
            """Ирина:
Линейка 4
Максим:
Ручка 1
Тетрадь 6
Николай:
Карандаш 3""",
        ),
        # Два покупателя, разные товары
        (
            """4
Анна Яблоко 5
Борис Банан 3
Анна Груша 2
Борис Яблоко 1""",
            """Анна:
Груша 2
Яблоко 5
Борис:
Банан 3
Яблоко 1""",
        ),
        # Один покупатель, много товаров
        (
            """3
Пётр Молоко 2
Пётр Хлеб 1
Пётр Молоко 3""",
            """Пётр:
Молоко 5
Хлеб 1""",
        ),
        # Разные покупатели, один товар
        (
            """3
Катя Книга 2
Миша Книга 1
Оля Книга 3""",
            """Катя:
Книга 2
Миша:
Книга 1
Оля:
Книга 3""",
        ),
        # Минимум данных
        (
            """1
Иван Ручка 5""",
            """Иван:
Ручка 5""",
        ),
    ],
)
def test_10_7_8(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_10_7_8()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected.strip()
