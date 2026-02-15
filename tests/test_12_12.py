import pytest
from src.module_12 import (
    m_12_12_1,
    m_12_12_2,
    m_12_12_3,
    m_12_12_4,
    m_12_12_5,
    m_12_12_6,
    m_12_12_7,
    m_12_12_8,
    m_12_12_9,
    m_12_12_10,
    m_12_12_11,
    m_12_12_12,
    m_12_12_13,
    m_12_12_14,
    m_12_12_15,
    m_12_12_16,
)


# m_12_12_1: Конвертер температур для нескольких значений
@pytest.mark.parametrize(
    "temps, expected",
    [
        # Sample Input: 15→59.0, 19→66.2, 10→50.0, 30→86.0, 9→48.2
        ((15, 19, 10, 30, 9), [59.0, 66.2, 50.0, 86.0, 48.2]),
        # Пустой список → пустой результат
        ((), []),
        # Одна температура: 0°C → 32°F
        ((0,), [32.0]),
        # Отрицательные: -10°C → 14°F
        ((-10, -5, 0), [14.0, 23.0, 32.0]),
        # Десятичные: 25.5°C → 77.9°F
        ((25.5, 37.0), [77.9, 98.6]),
    ],
)
def test_12_12_01(temps, expected):
    result = m_12_12_1(*temps)
    assert result == expected


# m_12_12_2: Генератор для пакетной обработки данных
@pytest.mark.parametrize(
    "data, batch_size, expected",
    [
        # Sample Input: [1,2,3,4,5,6] по 2 → 3 батча
        ([1, 2, 3, 4, 5, 6], 2, [[1, 2], [3, 4], [5, 6]]),
        # Последний батч меньше: 7 элементов по 3
        ([10, 20, 30, 40, 50, 60, 70], 3, [[10, 20, 30], [40, 50, 60], [70]]),
        # Пустой список → пустой генератор
        ([], 2, []),
        # Разные типы данных: строки + числа
        (["a", "b", "c", "d"], 2, [["a", "b"], ["c", "d"]]),
        # batch_size > len(data) → один батч
        ([100, 200, 300], 5, [[100, 200, 300]]),
    ],
)
def test_12_12_2(data, batch_size, expected):
    result = list(m_12_12_2(data, batch_size))  # Преобразуем генератор в список
    assert result == expected


# m_12_12_3: Анализатор оценок студентов
@pytest.mark.parametrize(
    "grades, expected",
    [
        # Sample Input: 5,5,3,4,5 → avg=4.4, max=5, min=3
        ((5, 5, 3, 4, 5), {"average": 4.4, "max": 5, "min": 3}),
        # Две оценки: 10, 2 → avg=6.0
        ((10, 2), {"average": 6.0, "max": 10, "min": 2}),
        # Все одинаковые: avg=max=min
        ((7, 7, 7), {"average": 7.0, "max": 7, "min": 7}),
        # Десятичные оценки
        ((4.5, 3.2, 5.0), {"average": 4.2, "max": 5.0, "min": 3.2}),
        # Большие разброс: 1, 10, 100
        ((1, 10, 100), {"average": 37.0, "max": 100, "min": 1}),
    ],
)
def test_12_12_3(grades, expected):
    result = m_12_12_3(*grades)
    assert result == expected


# m_12_12_4: Калькулятор скидок с параметрами по умолчанию
@pytest.mark.parametrize(
    "base_price, discount_percent, loyalty_discount, expected",
    [
        # Sample Input: 1000, default 10%, default 5% → 855.0
        (1000, 10, 5, 855.0),
        # Без скидок постоянных: только 10%
        (500, 10, 0, 450.0),
        # Только скидка постоянных
        (200, 0, 5, 190.0),
        # Кастомные скидки: 20% + 10%
        (1000, 20, 10, 720.0),
        # Маленькая цена с большими скидками
        (50, 30, 15, 29.8),
    ],
)
def test_12_12_4(base_price, discount_percent, loyalty_discount, expected):
    result = m_12_12_4(base_price, discount_percent, loyalty_discount)
    assert result == expected


# m_12_12_5: Функция с переменным числом аргументов и ключевых слов
@pytest.mark.parametrize(
    "args, kwargs, expected",
    [
        # Sample Input: name, age + other_info + kwargs → полный словарь
        (
            ("Arthur", 32, "engineer", "music"),
            {"country": "Russia", "city": "Saint Petersburg", "hobby": "write code"},
            {
                "name": "Arthur",
                "age": 32,
                "other_info": ["engineer", "music"],
                "attributes": {
                    "country": "Russia",
                    "city": "Saint Petersburg",
                    "hobby": "write code",
                },
            },
        ),
        # Только name+age, без other_info и kwargs
        (
            ("Alice", 25),
            {},
            {"name": "Alice", "age": 25, "other_info": [], "attributes": {}},
        ),
        # Много other_info, без kwargs
        (
            ("Bob", 40, "doctor", "sports", "books"),
            {},
            {
                "name": "Bob",
                "age": 40,
                "other_info": ["doctor", "sports", "books"],
                "attributes": {},
            },
        ),
        # Без other_info, только kwargs
        (
            ("Eve", 28),
            {"job": "teacher", "city": "Moscow"},
            {
                "name": "Eve",
                "age": 28,
                "other_info": [],
                "attributes": {"job": "teacher", "city": "Moscow"},
            },
        ),
        # Всё вместе: name, age, other_info, kwargs
        (
            ("John", 35, "python", "tester"),
            {"lang": "ru", "exp": 5},
            {
                "name": "John",
                "age": 35,
                "other_info": ["python", "tester"],
                "attributes": {"lang": "ru", "exp": 5},
            },
        ),
    ],
)
def test_12_12_5(args, kwargs, expected):
    result = m_12_12_5(*args, **kwargs)
    assert result == expected


# m_12_12_6: Калькулятор пиццы для вечеринки
@pytest.mark.parametrize(
    "appetites, expected",
    [
        # Sample Input: ср(3)+больш(4)+мал(2)+ср(3)+больш(4) = 16 + 2 = 18 → 3 пиццы
        (("средний", "большой", "малый", "средний", "большой"), 3),
        # Все малый аппетит: 5×2=10 + 2 = 12 → 2 пиццы
        (("малый", "малый", "малый", "малый", "малый"), 2),
        # Все большой: 3×4=12 + 2 = 14 → 2 пиццы
        (("большой", "большой", "большой"), 2),
        # Один гость средний: 3 + 2 = 5 → 1 пицца
        (("средний",), 1),
        # Смешанные: мал+ср+больш = 2+3+4=9 + 2 = 11 → 2 пиццы
        (("малый", "средний", "большой"), 2),
    ],
)
def test_12_12_6(appetites, expected):
    result = m_12_12_6(*appetites)
    assert result == expected


# m_12_12_7: Калькулятор рецепта
@pytest.mark.parametrize(
    "recipe, from_portions, to_portions, expected",
    [
        # Sample Input: ×1.5 коэффициент
        (
            {"мука": 200, "сахар": 100, "молоко": 0.5, "яйца": 2},
            4,
            6,
            {"мука": 300, "сахар": 150, "молоко": 0.8, "яйца": 3},
        ),
        # Уменьшение порций: ×0.5
        (
            {"рис": 400, "вода": 0.8, "масло": 50},
            6,
            3,
            {"рис": 200, "вода": 0.4, "масло": 25},
        ),
        # Только целые (сыпучие)
        ({"соль": 10, "перец": 5}, 2, 4, {"соль": 20, "перец": 10}),
        # Только жидкости
        ({"вода": 1.0, "сок": 0.3}, 5, 10, {"вода": 2.0, "сок": 0.6}),
        # Смешанные + разные коэффициенты
        (
            {"овощи": 300, "бульон": 1.2, "специи": 8},
            3,
            5,
            {"овощи": 500, "бульон": 2.0, "специи": 13},
        ),
    ],
)
def test_12_12_7(recipe, from_portions, to_portions, expected):
    result = m_12_12_7(recipe, from_portions, to_portions)
    assert result == expected


# m_12_12_8: Бюджет на путешествие
@pytest.mark.parametrize(
    "days, people, kwargs, expected",
    [
        # Sample Input: 7 дней × 2 чел × (50+30+20+25) = 250 → +15% = 2012.50
        (
            7,
            2,
            {"hotel": 50, "food": 30, "transport": 20, "entertainment": 25},
            2012.50,
        ),
        (1, 1, {"food": 20}, 23.0),
        (3, 4, {"hotel": 100, "food": 50, "transport": 30}, 2484.0),
        (5, 2, {"hotel": 40, "food": 25}, 747.5),
        (10, 3, {"hotel": 60, "food": 40, "transport": 15, "excursions": 20}, 4657.5),
    ],
)
def test_12_12_8(days, people, kwargs, expected):
    result = m_12_12_8(days, people, **kwargs)
    assert abs(result - expected) < 0.01  # Учёт плавающей точки


# m_12_12_9: Декоратор для проверки типов аргументов
@pytest.mark.parametrize(
    "arg_types, args, expected",
    [
        ((int, int), (5, 3), 8),
        ((int, int), ("5", 3), "TypeError"),
        ((int, int), (1, True), "TypeError"),  # bool != int ✓
        ((str, float), (123, "3.14"), "TypeError"),
        ((str, str), ("3.14", "test"), "3.14test"),
    ],
)
def test_12_12_9(arg_types, args, expected):
    def test_func(a, b):
        return a + b

    type_check = m_12_12_9()
    decorator = type_check(*arg_types)
    checked_func = decorator(test_func)
    assert checked_func(*args) == expected


# m_12_12_10: Фабрика функций для математических операций
@pytest.mark.parametrize(
    "operation, args, expected",
    [
        # Sample Input: "add"(5, 3) → 8
        ("add", (5, 3), 8),
        # subtract: 10-4=6
        ("subtract", (10, 4), 6),
        # multiply: 6×7=42
        ("multiply", (6, 7), 42),
        # divide: 15/3=5.0
        ("divide", (15, 3), 5.0),
        # divide by zero → None
        ("divide", (10, 0), None),
    ],
)
def test_12_12_10(operation, args, expected):
    op_func = m_12_12_10(operation)

    # Вызываем созданную функцию
    result = op_func(*args)
    assert result == expected


# m_12_12_11: Расчет круглых конфет в цилиндрической ёмкости
@pytest.mark.parametrize(
    "height, diameter, candy_diameter, expected",
    [
        # Sample Input: D=100, h=150, d=20 → 180 конфет
        (100, 150, 20, 180),
        # Маленькая банка
        (60, 50, 10, 172),
        # Большая банка
        (300, 200, 30, 640),
        # Узкая высокая банка
        (40, 150, 15, 68),
        # Короткая широкая банка
        (200, 30, 25, 73),
    ],
)
def test_12_12_11(height, diameter, candy_diameter, expected):
    result = m_12_12_11(height, diameter, candy_diameter)
    assert result == expected


# m_12_12_12: Калькулятор мозаики для ремонта
@pytest.mark.parametrize(
    "wall_height_cm, wall_width_cm, mosaic_area, openings, expected",
    [
        # Sample Input: 300×500=150000 см² = 15 м² → 15/0.25=60 панелей
        (300, 500, 0.25, [], 60),
        # Одно окно: вычитаем 100×100 см
        (
            300,
            500,
            0.25,
            [
                (100, 100, 1),
            ],
            56,
        ),
        (250, 400, 0.2, [(80, 120, 1), (60, 60, 2)], 42),
        (400, 600, 0.5, [], 48),
        (400, 600, 1.1, [], 22),
        (200, 300, 0.1, [(50, 50, 3)], 53),
    ],
)
def test_12_12_12(wall_height_cm, wall_width_cm, mosaic_area, openings, expected):
    result = m_12_12_12(wall_height_cm, wall_width_cm, mosaic_area, openings)
    assert result == expected


# m_12_12_13: Рекурсивный обход вложенных структур
@pytest.mark.parametrize(
    "structure, expected",
    [
        # Sample Input: True(игнор)+2+[3,4,[5,6]]+7+(8,9) = 44
        ([True, 2, [3, 4, [5, 6]], 7, (8, 9)], 44),
        # Простой список чисел
        ([1, 2, 3, 4], 10),
        # Глубокая вложенность
        ([1, [2, [3, [4]]]], 10),
        # Смешанные типы: числа + игнорируемые
        ([1, "text", [2, None, 3], True, (4, 5)], 15),
        # Кортеж с вложенными списками
        ((1, [2, 3], (4, [5])), 15),
    ],
)
def test_12_12_13(structure, expected):
    result = m_12_12_13(structure)
    assert result == expected


# m_12_12_14: Декоратор для отладки функций
@pytest.mark.parametrize(
    "args, kwargs, expected_result",
    [
        # Sample Input: add_numbers(7, y=5) → 12
        ((7,), {"y": 5}, 12),
        # Только позиционные аргументы
        ((10, 20), {}, 30),
        # Только kwargs
        ((), {"a": 3, "b": 4}, 7),
        # Смешанные аргументы
        ((1, 2), {"multiply": 0}, 3),
        # Один аргумент
        ((42,), {}, 42),
    ],
)
def test_12_12_14(args, kwargs, expected_result, capsys):

    def test_func(*args, **kwargs):
        res = sum(args) + sum(kwargs.values())
        return res

    debugged_func = m_12_12_14(test_func)
    result = debugged_func(*args, **kwargs)
    assert result == expected_result
    captured = capsys.readouterr()
    assert (
        f"Вызвана функция test_func с аргументами: args: {args} kwargs: {kwargs}"
        in captured.out
    )
    assert f"test_func вернула значение: {expected_result}" in captured.out


# m_12_12_15: Декоратор для обработки исключений
@pytest.mark.parametrize(
    "args, expected",
    [
        # Sample Input: 10/0 → ZeroDivisionError
        ((10, 0), "Произошла ошибка: division by zero"),
        (("abc",), "Произошла ошибка: invalid literal for int() with base 10: 'abc'"),
        (
            ("hello", 5),
            "Произошла ошибка: invalid literal for int() with base 10: 'hello'",
        ),
        (
            ([1, 2, 3], 99),
            "Произошла ошибка: unsupported operand type(s) for /: 'list' and 'int'",
        ),
        ((10, 2), 5.0),
    ],
)
def test_12_12_15(args, expected):
    def divide(a, b=2):
        if isinstance(a, str):
            int(a)
        return a / b

    handler = m_12_12_15()
    safe_divide = handler(divide)

    assert safe_divide(*args) == expected


# m_12_12_16: Декоратор для валидации входных данных
@pytest.mark.parametrize(
    "validators, args, expected",
    [
        # Sample Input: x>0, y=str → "Hello"*3
        (
            (lambda x: x > 0, lambda y: isinstance(y, str)),
            (3, "Hello"),
            "HelloHelloHello",
        ),
        # Ошибка: x≤0
        (
            (lambda x: x > 0, lambda y: isinstance(y, str)),
            (0, "test"),
            "Ошибка валидации",
        ),
        # Ошибка: y не строка
        (
            (lambda x: x > 0, lambda y: isinstance(y, str)),
            (5, 123),
            "Ошибка валидации",
        ),
        # Один валидатор
        ((lambda x: x >= 0,), (42,), ""),
        # Несколько валидаторов + сложная логика
        ((lambda x: x > 0, lambda y: len(y) > 3), (2, "python"), "pythonpython"),
    ],
)
def test_12_12_16(validators, args, expected):
    def test_func(x, y=""):
        return str(y) * x

    validate_input = m_12_12_16()(*validators)
    result = validate_input(test_func)(*args)
    assert result == expected
