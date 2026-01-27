import pytest
from src.module_10 import (
    m_10_6_1,
    m_10_6_2,
    m_10_6_3,
    m_10_6_4,
    m_10_6_5,
    m_10_6_6,
    m_10_6_7,
    m_10_6_8,
    m_10_6_9,
    m_10_6_10,
    m_10_6_11,
    m_10_6_12,
    m_10_6_13,
    m_10_6_14,
    m_10_6_15,
)


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ('{"a": 1, "b": 2, "c": 3}', "3"),
        ("{}", "0"),
        ('{"a": 1, "b": 2}', "2"),
        ('{"key": "value"}', "1"),
    ],
)
def test_10_6_01(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_10_6_1()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            '{"red": "#FF0000", "green": "#00FF00"}\n{"blue": "#0000FF",'
            ' "white": "#FFFFFF"}',
            "blue - #0000FF\ngreen - #00FF00\nred - #FF0000\nwhite - #FFFFFF",
        ),
        (
            '{"a": 1}\n{"b": 2}',
            "a - 1\nb - 2",
        ),
        (
            '{"z": 26, "y": 25}\n{"x": 24}',
            "x - 24\ny - 25\nz - 26",
        ),
        ('{}\n{"one": 1}', "one - 1"),
        ('{"first": "A"}\n{}', "first - A"),
    ],
)
def test_10_6_2(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=input_data.split("\n"))
    m_10_6_2()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            '{"name": "Arthur", "age": 30, "major": "Engineering"}',
            "major - Engineering",
        ),
        ('{"first": 1, "second": 2, "third": 3}', "third - 3"),
        ('{"a": "alpha", "b": "beta"}', "b - beta"),
        ('{"single": "only"}', "single - only"),
        ("{}", "Невозможно удалить. Словарь пустой."),
    ],
)
def test_10_6_3(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_10_6_3()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            '{1: "Один", 2: "Два", 3: "Три", 5: "пять", 10: "Десять", 20: "Двадцать", 100: "сто"}',
            "141\n100\n1\n7",
        ),
        ('{1: "a", 3: "b", 5: "c"}', "9\n5\n1\n3"),
        ('{10: "x", 20: "y", 30: "z"}', "60\n30\n10\n3"),
        ('{100: "big"}', "100\n100\n100\n1"),
        ('{1: "small", 2: "med"}', "3\n2\n1\n2"),
    ],
)
def test_10_6_4(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_10_6_4()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ('{"year": 2024, "month": 9, "day": 3}', "03.09.2024"),
        ('{"year": 2023, "month": 12, "day": 25}', "25.12.2023"),
        ('{"year": 999, "month": 1, "day": 1}', "01.01.0999"),
        ('{"year": 2025, "month": 5, "day": 15}', "15.05.2025"),
        ('{"year": 2000, "month": 10, "day": 10}', "10.10.2000"),
    ],
)
def test_10_6_5(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_10_6_5()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (
            '{"love": "любовь", "family": "семья", "work": "работа", '
            '"tree": "дерево", "city": "город", "music": "музыка", '
            '"beach": "пляж"}\n9\nfamily\nmusic\ncity\nwork\nhouse\nlove\ntree\nrain\nsnow',
            "семья\nмузыка\nгород\nработа\nНе найдено\nлюбовь\nдерево\nНе найдено\nНе найдено",
        ),
        (
            '{"cat": "кот", "dog": "собака"}\n3\ncat\ndog\nbird',
            "кот\nсобака\nНе найдено",
        ),
        (
            '{"hello": "привет"}\n1\nhello',
            "привет",
        ),
        (
            "{} \n2\none\ntwo",
            "Не найдено\nНе найдено",
        ),
        (
            '{"a": "alpha"}\n4\na\nb\na\nc',
            "alpha\nНе найдено\nalpha\nНе найдено",
        ),
    ],
)
def test_10_6_6(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_10_6_6()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (
            '{"а": "г", "б": "д", "в": "е", "г": "ё", "д": "ж", "е": "з",'
            ' "ё": "и", "ж": "й", "з": "к", "и": "л", "й": "м", "к": "н", "л":'
            ' "о", "м": "п", "н": "р", "о": "с", "п": "т", "р": "у", "с": "ф",'
            ' "т": "х", "у": "ц", "ф": "ч", "х": "ш", "ц": "щ", "ч": "ъ", "ш":'
            ' "ы", "щ": "ь", "ъ": "э", "ы": "ю", "ь": "я", "э": "а", "ю": "б",'
            ' "я": "в"}\nмнёявп, фёпэвхщ ъпл? тв тв :)',
            "привет, читаешь это? хе хе :)",
        ),
        (
            '{"a": "1", "b": "2"}\nabc',
            "12c",
        ),
        (
            '{"x": "X", "y": "Y"}\nxyz',
            "XYz",
        ),
        (
            "{} \nhello",
            "hello",
        ),
        (
            '{"1": "one"}\n123',
            "one23",
        ),
    ],
)
def test_10_6_7(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_10_6_7()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            "Море волнуется раз, море волнуется два, море волнуется три.",
            "1\n1\n1\n2\n2\n1\n3\n3\n1",
        ),
        ("hello world hello", "1\n1\n2"),
        ("a b c b a", "1\n1\n1\n2\n2"),
        ("test test test", "1\n2\n3"),
        ("one two three two one", "1\n1\n1\n2\n2"),
    ],
)
def test_10_6_8(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_10_6_8()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("1993", "MCMXCIII"),
        ("2024", "MMXXIV"),
        ("1", "I"),
        ("1000", "M"),
        ("1492", "MCDXCII"),
    ],
)
def test_10_6_9(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_10_6_9()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (
            "12\nРоссия\nТурция\nИталия\nРоссия\nИталия\nКитай\nКитай\nИталия"
            "\nРоссия\nТурция\nРоссия\nТурция",
            "Италия: 3\nКитай: 2\nРоссия: 4\nТурция: 3",
        ),
        (
            "5\nUSA\nUSA\nUK\nFrance\nUK",
            "France: 1\nUK: 2\nUSA: 2",
        ),
        (
            "3\nA\nA\nA",
            "A: 3",
        ),
        (
            "4\ncat\ndog\ncat\ndog",
            "cat: 2\ndog: 2",
        ),
        (
            "1\nMoscow",
            "Moscow: 1",
        ),
    ],
)
def test_10_6_10(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_10_6_10()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Привет, мир!", "11"),
        ("кот", "4"),  # к2 + о1 + т1 = 4
        ("абв", "5"),  # а1 + б3 + в1 = 5
        ("жизнь", "15"),  # ж5 + и1 + з5 + н1 + ь3 = 15
        ("шёл", "13"),  # ш8 + ё3 + л2 = 13
        ("фь", "13"),  # ф10 + ь3 = 13
    ],
)
def test_10_6_11(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_10_6_11()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        ("Иванов Иван Иванович", "Ivanov Ivan Ivanovich"),
        ("Петров Петр Петрович", "Petrov Petr Petrovich"),
        ("Сидорова Анна Сергеевна", "Sidorova Anna Sergeevna"),
        ("Жуков Женя Жанович", "Zhukov Zhenja Zhanovich"),
        ("Щукина Юлия Юрьевна", "Schukina Julija Jurevna"),
    ],
)
def test_10_6_12(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_10_6_12()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (
            "Иванов Смирнов Сидоров\n6\nИванов: 8\nСмирнов: 7\nСидоров: 9\nИванов: 6\nСмирнов: 7\nСидоров: 4",
            "Иванов: 14\nСидоров: 13\nСмирнов: 14",
        ),
        (
            "Петров Иванов\n2\nПетров: 5\nИванов: 3",
            "Иванов: 3\nПетров: 5",
        ),
        (
            "А Б\n3\nА: 10\nБ: 20\nА: 5",
            "А: 15\nБ: 20",
        ),
        (
            "Один\n1\nОдин: 100",
            "Один: 100",
        ),
        (
            "X Y\n0",
            "X: 0\nY: 0",
        ),
    ],
)
def test_10_6_13(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_10_6_13()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "input_data, expected",
    [
        (
            "Ghbdtn/ F ns pyfk? xnj cbyuekzhyjcnm tcnm yt htfkmysq abpbxtcrbq j,]trn? f abpbxtcrfz vjltkm bkb f,cnhfrwbz",
            "Привет. А ты знал, что сингулярность есть не реальный физический объект, а физическая модель или абстракция",
        ),
        ("Hello", "Руддщ"),
        ("123 qwe", "123 йцу"),
        ("Abc 123", "Фис 123"),
        ("!@#", '!"№'),
    ],
)
def test_10_6_14(input_data, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_data)
    m_10_6_14()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (
            "12\nPython: Интерпретируемый, высокоуровневый язык программирования\nИнтерпретатор: Программа, выполняющая код построчно\nПеременная: Именованная область памяти для хранения данных\nФункция: Блок кода для выполнения задачи\nЦикл: Структура для многократного выполнения кода\nУсловие: Конструкция для проверки условия и выполнения кода\nКласс: Шаблон для создания объектов\nМетод: Функция, принадлежащая классу\nМодуль: Файл с кодом, содержащий переменные и функции\nСписок: Упорядоченная коллекция элементов\nИндексация: Обращение к элементам коллекции по их позициям\nСловарь: Коллекция пар ключ-значение\n7\nИнтерпретатор\nУсловие\nВот эта штука\nПеременная\nВаййяя\nПодкрадули\nСловарь",
            "Программа, выполняющая код построчно\nКонструкция для проверки условия и выполнения кода\nНе найдено\nИменованная область памяти для хранения данных\nНе найдено\nНе найдено\nКоллекция пар ключ-значение",
        ),
        (
            "2\ncat: кошка\ndog: собака\n3\ncat\ndog\nbird",
            "кошка\nсобака\nНе найдено",
        ),
        (
            "1\nhello: привет\n2\nhello\nworld",
            "привет\nНе найдено",
        ),
        (
            "0\n1\nterm",
            "Не найдено",
        ),
        (
            "3\nA: 1\nB: 2\nA: 1\n2\nA\nB",
            "1\n2",
        ),
    ],
)
def test_10_6_15(inputs, expected, mocker, capsys):
    mocker.patch("builtins.input", side_effect=inputs.split("\n"))
    m_10_6_15()
    captured = capsys.readouterr()
    assert captured.out.strip() == expected
