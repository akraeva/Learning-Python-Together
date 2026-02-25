import pytest
from pathlib import Path
from src.module_13 import (
    m_13_3_1,
    m_13_3_2,
    m_13_3_3,
    m_13_3_4,
    m_13_3_5,
    m_13_3_6,
    m_13_3_7,
    m_13_3_8,
    m_13_3_9,
    m_13_3_10,
    m_13_3_11,
    m_13_3_12,
    m_13_3_13,
    m_13_3_14,
    m_13_3_15,
)


# m_13_3_1: Караоке
@pytest.mark.parametrize(
    "filename, content, expected",
    [
        # Sample Input: 3 строки с переносами
        (
            "text_file1.txt",
            "If I stay with you, if I'm choosing wrong\nI don't care at all\nIf I'm losing now, but I'm winning late\n",
            "If I stay with you, if I'm choosing wrong\nI don't care at all\nIf I'm losing now, but I'm winning late\n",
        ),
        # Одна строка без переноса
        ("single_line.txt", "Hello, World!", "Hello, World!"),
        # Пустой файл
        ("empty.txt", "", ""),
        # Файл с русским текстом + переносами
        (
            "russian.txt",
            "Привет, мир!\nЭто тест.\nПоследняя строка.",
            "Привет, мир!\nЭто тест.\nПоследняя строка.",
        ),
    ],
)
def test_13_3_1(filename, content, expected, mocker, capsys):
    mocker.patch("builtins.input", return_value=filename)
    file_path = Path(".") / filename
    file_path.write_text(content, encoding="utf-8")
    m_13_3_1()

    captured = capsys.readouterr()
    assert captured.out.rstrip() == expected.rstrip()
    file_path.unlink(missing_ok=True)


# m_13_3_2: Система резервного копирования
@pytest.mark.parametrize(
    "filename, content",
    [
        # Тест 1: Обычный файл .txt (как в Sample Input)
        (
            "orig_text1.txt",
            "Привет, мир!\nЭто тестовый файл для резервного копирования.\nСодержит обычный текст без специальных символов.\n",
        ),
        # Тест 2: Файл с другим расширением (.py)
        (
            "script.py",
            "def backup():\n    pass\n",
        ),
        # Тест 3: Файл с длинным именем
        (
            "my_important_document_2025.txt",
            "Важные данные\nСтрока 2\nСтрока 3\n",
        ),
        # Тест 4: Файл с русским именем
        (
            "документ.txt",
            "Тестовый файл\nС русским именем\n",
        ),
    ],
)
def test_13_3_2(filename, content, mocker):
    mocker.patch("builtins.input", return_value=filename)
    file_path = Path(".") / filename
    file_path.write_text(content, encoding="utf-8")

    m_13_3_2()

    name_without_ext = file_path.stem
    ext = file_path.suffix
    expected_backup_name = f"{name_without_ext}_19.11.2025{ext}"
    backup_path = Path(".") / expected_backup_name

    assert backup_path.exists()
    backup_content = backup_path.read_text(encoding="utf-8")
    assert backup_content == content

    assert file_path.read_text(encoding="utf-8") == content
    file_path.unlink(missing_ok=True)
    backup_path.unlink(missing_ok=True)


# m_13_3_3: Анализ текста
@pytest.mark.parametrize(
    "filename, content, expected_lines, expected_words, expected_longest",
    [
        # Тест 1: Sample Input
        (
            "text_file1.txt",
            "Как упоительны в России вечера,\nЛюбовь, шампанское, закаты, переулки,\nАх, лето красное, забавы и прогулки,\nКак упоительны в России вечера.\n",
            4,
            20,
            "Любовь, шампанское, закаты, переулки,",
        ),
        # Тест 2: Пустой файл
        ("empty.txt", "", 0, 0, ""),
        # Тест 3: Одна строка
        ("single.txt", "Только одно слово", 1, 3, "Только одно слово"),
        # Тест 4: Файл с разной длиной строк
        (
            "various.txt",
            "a\n" "очень длинная строка с многими символами\n" "bbb\n",
            3,
            8,
            "очень длинная строка с многими символами",
        ),
        # Тест 5: Русский текст + цифры
        (
            "russian_stats.txt",
            "Привет мир!\n"
            "Это тестовая строка 123\n"
            "Самая длинная строка содержит пробелы и знаки препинания!!!",
            3,
            14,
            "Самая длинная строка содержит пробелы и знаки препинания!!!",
        ),
    ],
)
def test_13_3_3(
    filename,
    content,
    expected_lines,
    expected_words,
    expected_longest,
    mocker,
    capsys,
):
    """Тест для m_13_3_3: анализ статистики файла."""
    mocker.patch("builtins.input", return_value=filename)

    file_path = Path(".") / filename
    file_path.write_text(content, encoding="utf-8")

    m_13_3_3()

    captured = capsys.readouterr()
    expected_output = (
        f"Статистика файла {filename}:\n"
        f"Количество строк: {expected_lines}\n"
        f"Количество слов: {expected_words}\n"
        f"Самая длинная строка: {expected_longest}\n"
    )

    assert captured.out == expected_output
    file_path.unlink(missing_ok=True)


# m_13_3_4: Список покупок
@pytest.mark.parametrize(
    "filename, content, inputs, expected_content",
    [
        # Тест 1: Sample Input
        (
            "file_with_purchases1.txt",
            "",
            [
                "file_with_purchases1.txt",
                "  СЫР  ",
                "колбаса:",
                "  молоко  ",
                "Хлеб,",
                "Яйца.",
                "бананы  ;  ",
                "  апельсины.  ",
                "0",
            ],
            "- Сыр\n- Колбаса\n- Молоко\n- Хлеб\n- Яйца\n- Бананы\n- Апельсины\n",
        ),
        # Тест 2: Пустой список (только 0)
        ("empty_list.txt", "", ["empty_list.txt", "0"], ""),
        # Тест 3: Один товар с лишними символами
        (
            "single_item.txt",
            "",
            ["single_item.txt", "  тестовый текст:  ", "0"],
            "- Тестовый текст\n",
        ),
        # Тест 4: Смешанный регистр + пробелы
        (
            "mixed_case.txt",
            "",
            ["mixed_case.txt", "КОФЕ", "   ЧАЙ   ,,", "сахар.", "0"],
            "- Кофе\n- Чай\n- Сахар\n",
        ),
        # Тест 5: Кириллица + латиница
        (
            "multilang.txt",
            "",
            ["multilang.txt", "Продукты ,", "Milk  ;", "Молоко:", "0"],
            "- Продукты\n- Milk\n- Молоко\n",
        ),
    ],
)
def test_13_3_4(filename, inputs, expected_content, mocker, content):
    mocker.patch("builtins.input", side_effect=inputs)
    file_path = Path(".") / filename
    file_path.write_text(content, encoding="utf-8")
    m_13_3_4()
    result_content = file_path.read_text(encoding="utf-8")
    assert result_content == expected_content
    file_path.unlink(missing_ok=True)


# m_13_3_5: Список покупок, новые товары
@pytest.mark.parametrize(
    "filename, content, inputs, expected_content",
    [
        # Тест 1: Sample Input (дописываем к существующему содержимому)
        (
            "file_with_purchases1.txt",
            "- Яблоки\n- Груши\n",  # ← ИСХОДНОЕ содержимое
            [
                "file_with_purchases1.txt",  # Имя файла
                "  СЫР  ",
                "колбаса:",
                "  молоко  ",
                "Хлеб,",
                "Яйца.",
                "бананы  ;  ",
                "  апельсины.  ",
                "0",
            ],
            "- Яблоки\n- Груши\n- Сыр\n- Колбаса\n- Молоко\n- Хлеб\n- Яйца\n- Бананы\n- Апельсины\n",
        ),
        # Тест 2: Пустой список (дописываем к существующему)
        (
            "empty_list.txt",
            "Предыдущие покупки:\n- Хлеб\n",
            ["empty_list.txt", "0"],
            "Предыдущие покупки:\n- Хлеб\n",  # Ничего не добавилось
        ),
        # Тест 3: Один товар (дописываем к существующему)
        (
            "single_item.txt",
            "",
            ["single_item.txt", "  тестовый текст:  ", "0"],
            "- Тестовый текст\n",
        ),
        # Тест 4: Смешанный регистр (дописываем многострочное содержимое)
        (
            "mixed_case.txt",
            "- Масло\n- Соль\n",
            ["mixed_case.txt", "КОФЕ", "   ЧАЙ   ,,", "сахар.", "0"],
            "- Масло\n- Соль\n- Кофе\n- Чай\n- Сахар\n",
        ),
        # Тест 5: Кириллица + латиница (дописываем к файлу с кириллицей)
        (
            "multilang.txt",
            "Мои продукты:\n- Картошка\n",
            ["multilang.txt", "Продукты ,", "Milk  ;", "Молоко:", "0"],
            "Мои продукты:\n- Картошка\n- Продукты\n- Milk\n- Молоко\n",
        ),
    ],
)
def test_13_3_5(filename, inputs, expected_content, mocker, content):
    mocker.patch("builtins.input", side_effect=inputs)
    file_path = Path(".") / filename
    file_path.write_text(content, encoding="utf-8")
    m_13_3_5()
    result_content = file_path.read_text(encoding="utf-8")
    assert result_content == expected_content
    file_path.unlink(missing_ok=True)


# m_13_3_6: Конвертер температур
@pytest.mark.parametrize(
    "input_filename, output_filename, input_content, inputs, expected_output_content",
    [
        # Тест 1: Sample Input
        (
            "celsius1.txt",
            "fahrenheit1.txt",
            "0.0\n7.3\n20.1\n37.3\n100\n",
            ["celsius1.txt", "fahrenheit1.txt"],
            "32.0\n45.1\n68.2\n99.1\n212.0\n",
        ),
        # Тест 2: Отрицательные температуры
        (
            "negative.txt",
            "negative_f.txt",
            "-17.8\n-40\n",
            ["negative.txt", "negative_f.txt"],
            "0.0\n-40.0\n",
        ),
        # Тест 3: Один элемент
        (
            "single.txt",
            "single_f.txt",
            "25\n",
            ["single.txt", "single_f.txt"],
            "77.0\n",
        ),
        # Тест 4: Десятичные дроби
        (
            "decimals.txt",
            "decimals_f.txt",
            "23.5\n-12.7\n36.6\n",
            ["decimals.txt", "decimals_f.txt"],
            "74.3\n9.1\n97.9\n",
        ),
        # Тест 5: Нулевые значения
        (
            "zeros.txt",
            "zeros_f.txt",
            "0\n0.0\n",
            ["zeros.txt", "zeros_f.txt"],
            "32.0\n32.0\n",
        ),
    ],
)
def test_13_3_6(
    input_filename,
    output_filename,
    input_content,
    inputs,
    expected_output_content,
    mocker,
):
    input_path = Path(".") / input_filename
    input_path.write_text(input_content, encoding="utf-8")
    mocker.patch("builtins.input", side_effect=inputs)
    m_13_3_6()
    output_path = Path(".") / output_filename
    assert output_path.exists()

    result_content = output_path.read_text(encoding="utf-8")
    assert result_content == expected_output_content
    input_path.unlink(missing_ok=True)
    output_path.unlink(missing_ok=True)


# m_13_3_7: Анализ успеваемости
@pytest.mark.parametrize(
    "input_file, output_file, input_content, expected_output",
    [
        # Тест 1: Sample Input (5 оценок → среднее 4.2)
        (
            "grades1.txt",
            "grades_report1.txt",
            "5\n3\n5\n4\n4\n",
            "Статистика из файла grades1.txt:\n"
            "Максимальная оценка: 5\n"
            "Минимальная оценка: 3\n"
            "Количество оценок: 5\n"
            "Средний балл: 4.2\n",
        ),
        # Тест 2: Только минимальные оценки
        (
            "all_threes.txt",
            "all_threes_report.txt",
            "3\n3\n3\n",
            "Статистика из файла all_threes.txt:\n"
            "Максимальная оценка: 3\n"
            "Минимальная оценка: 3\n"
            "Количество оценок: 3\n"
            "Средний балл: 3.0\n",
        ),
        # Тест 3: Максимальная разбросанность (2-5)
        (
            "spread_grades.txt",
            "spread_report.txt",
            "2\n5\n2\n5\n4\n3\n",
            "Статистика из файла spread_grades.txt:\n"
            "Максимальная оценка: 5\n"
            "Минимальная оценка: 2\n"
            "Количество оценок: 6\n"
            "Средний балл: 3.5\n",
        ),
        # Тест 4: Одна оценка
        (
            "single_grade.txt",
            "single_report.txt",
            "4\n",
            "Статистика из файла single_grade.txt:\n"
            "Максимальная оценка: 4\n"
            "Минимальная оценка: 4\n"
            "Количество оценок: 1\n"
            "Средний балл: 4.0\n",
        ),
    ],
)
def test_13_3_7(input_file, output_file, input_content, expected_output, mocker):
    input_path = Path(".") / input_file
    input_path.write_text(input_content, encoding="utf-8")

    mocker.patch("builtins.input", side_effect=[input_file, output_file])
    m_13_3_7()
    output_path = Path(".") / output_file
    assert output_path.exists()
    result_content = output_path.read_text(encoding="utf-8")
    assert result_content == expected_output
    input_path.unlink(missing_ok=True)
    output_path.unlink(missing_ok=True)


# m_13_3_8: Разделитель чисел
@pytest.mark.parametrize(
    "input_filename, even_filename, odd_filename, input_content, expected_even, expected_odd",
    [
        # Тест 1: Sample Input
        (
            "numbers1.txt",
            "even1.txt",
            "odd1.txt",
            "1\n2\n3\n4\n5\n",
            "2\n4\n",
            "1\n3\n5\n",
        ),
        # Тест 2: Только четные числа
        (
            "only_even.txt",
            "even_only.txt",
            "odd_only.txt",
            "10\n2\n100\n4\n",
            "10\n2\n100\n4\n",
            "",
        ),
        # Тест 3: Только нечетные + пустой файл
        (
            "only_odd.txt",
            "even_empty.txt",
            "odd_result.txt",
            "1\n3\n5\n7\n9\n",
            "",
            "1\n3\n5\n7\n9\n",
        ),
    ],
)
def test_13_3_8(
    input_filename,
    even_filename,
    odd_filename,
    input_content,
    expected_even,
    expected_odd,
    mocker,
):
    input_path = Path(".") / input_filename
    input_path.write_text(input_content, encoding="utf-8")
    mocker.patch(
        "builtins.input", side_effect=[input_filename, even_filename, odd_filename]
    )
    m_13_3_8()
    even_path = Path(".") / even_filename
    odd_path = Path(".") / odd_filename

    assert even_path.exists()
    assert odd_path.exists()

    even_content = even_path.read_text(encoding="utf-8")
    odd_content = odd_path.read_text(encoding="utf-8")

    assert even_content.rstrip() == expected_even.rstrip()
    assert odd_content.rstrip() == expected_odd.rstrip()

    input_path.unlink(missing_ok=True)
    even_path.unlink(missing_ok=True)
    odd_path.unlink(missing_ok=True)


# m_13_3_9: Библиотечный каталог
@pytest.mark.parametrize(
    "input_filename, input_content, expected_output",
    [
        # Тест 1: Sample Input
        (
            "books1.txt",
            "Мастер и Маргарита;Булгаков Михаил;1966;Роман;480\n"
            "Преступление и наказание;Достоевский Фёдор;1866;Роман;608\n"
            "Герой нашего времени;Лермонтов Михаил;1840;Роман;224\n",
            "{1: {'title': 'Мастер и Маргарита', 'author': 'Булгаков Михаил',"
            " 'year': 1966, 'genre': 'Роман', 'pages': 480}, "
            "2: {'title': 'Преступление и наказание', 'author': 'Достоевский"
            " Фёдор', 'year': 1866, 'genre': 'Роман', 'pages': 608}, "
            "3: {'title': 'Герой нашего времени', 'author': 'Лермонтов"
            " Михаил', 'year': 1840, 'genre': 'Роман', 'pages': 224}}\n",
        ),
        # Тест 2: Одна книга
        (
            "single_book.txt",
            "Война и мир;Толстой Лев;1869;Роман;1225\n",
            "{1: {'title': 'Война и мир', 'author': 'Толстой Лев', 'year':"
            " 1869, 'genre': 'Роман', 'pages': 1225}}\n",
        ),
        # Тест 3: Разные жанры + короткие названия
        (
            "mixed_genres.txt",
            "1984;Оруэлл Джордж;1949;Антиутопия;328\n"
            "Алхимик;Коэльо Пауло;1988;Философия;208\n"
            "Шерлок Холмс;Дойл Артур;1892;Детектив;288\n",
            "{1: {'title': '1984', 'author': 'Оруэлл Джордж', 'year': 1949,"
            " 'genre': 'Антиутопия', 'pages': 328}, "
            "2: {'title': 'Алхимик', 'author': 'Коэльо Пауло', 'year': 1988,"
            " 'genre': 'Философия', 'pages': 208}, "
            "3: {'title': 'Шерлок Холмс', 'author': 'Дойл Артур', 'year': 1892"
            ", 'genre': 'Детектив', 'pages': 288}}\n",
        ),
    ],
)
def test_13_3_9(input_filename, input_content, expected_output, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_filename)

    file_path = Path(".") / input_filename
    file_path.write_text(input_content, encoding="utf-8")

    m_13_3_9()
    captured = capsys.readouterr()
    assert captured.out == expected_output
    file_path.unlink(missing_ok=True)


# m_13_3_10: Валидатор паролей
@pytest.mark.parametrize(
    "input_filename, output_filename, input_content, expected_output_content",
    [
        # Тест 1: Sample Input (3 надежных из 5)
        (
            "pass1.txt",
            "valid_pass1.txt",
            "Password1!nqwertyn\n"  # ✅ Надежный (все 4 правила)
            "qwerty123\n"  # ❌ Нет заглавной, нет спецсимвола
            "Qwerty123!\n"  # ✅ Надежный
            "A1!aaaaa\n"  # ✅ Надежный (длина 8)
            "pass\n",  # ❌ Короткий
            "Password1!nqwertyn\nQwerty123!\nA1!aaaaa\n",
        ),
        # Тест 2: Ни одного надежного пароля
        (
            "weak_passwords.txt",
            "valid_weak.txt",
            "abc\n"  # ❌ Короткий
            "Abcdefgh\n"  # ❌ Нет цифры, нет спецсимвола
            "12345678\n"  # ❌ Нет заглавной, нет спецсимвола
            "Abcdef12\n",  # ❌ Нет спецсимвола
            "",
        ),
        # Тест 3: Русские символы + спецсимволы
        (
            "russian_pass.txt",
            "valid_russian.txt",
            "Пароль123!\n"  # ✅ Надежный (кириллица + все правила)
            "ПаРоЛЬ12\n"  # ❌ Нет спецсимвола
            "Abc@Рус123Аа\n"  # ✅ Надежный (смешанный текст)
            "short!\n",  # ❌ Короткий
            "Пароль123!\nAbc@Рус123Аа\n",
        ),
    ],
)
def test_13_3_10(
    input_filename,
    output_filename,
    input_content,
    expected_output_content,
    mocker,
):
    input_path = Path(".") / input_filename
    input_path.write_text(input_content, encoding="utf-8")
    mocker.patch("builtins.input", side_effect=[input_filename, output_filename])

    m_13_3_10()
    output_path = Path(".") / output_filename
    result_content = output_path.read_text(encoding="utf-8")
    assert result_content == expected_output_content
    input_path.unlink(missing_ok=True)
    output_path.unlink(missing_ok=True)


# m_13_3_11: Космический сканер
@pytest.mark.parametrize(
    "coords_filename, input_filename, output_filename, coords_content, map_content, expected_message, expected_output_map",
    [
        # Тест 1: Sample Input (попадание в астероид)
        (
            "coords_test1.txt",
            "field_test1.txt",
            "new_field_test1.txt",
            "3,2\n",
            "- * - - -\n" "- - * - -\n" "- * - * -\n" "- - - - *\n" "* - * - -\n",
            "Цель поражена\n",
            "- * - - -\n" "- - * - -\n" "- X - * -\n" "- - - - *\n" "* - * - -\n",
        ),
        # Тест 2: Промах (пустое место)
        (
            "coords_miss.txt",
            "field_miss.txt",
            "new_field_miss.txt",
            "2,3\n",
            "* - - *\n" "- * - -\n",
            "Промах\n",
            "* - - *\n" "- * . -\n",
        ),
        # Тест 3: Угловые координаты (попадание)
        (
            "coords_corner.txt",
            "field_corner.txt",
            "new_field_corner.txt",
            "3,1\n",
            "- - -\n* * *\n* - -\n",
            "Цель поражена\n",
            "- - -\n" "* * *\n" "X - -\n",
        ),
    ],
)
def test_13_3_11(
    coords_filename,
    input_filename,
    output_filename,
    coords_content,
    map_content,
    expected_message,
    expected_output_map,
    mocker,
    capsys,
):
    """Тест для m_13_3_11: космический сканер астероидов."""
    # Создаем файлы в текущей директории
    coords_path = Path(".") / coords_filename
    map_path = Path(".") / input_filename
    output_path = Path(".") / output_filename

    coords_path.write_text(coords_content, encoding="utf-8")
    map_path.write_text(map_content, encoding="utf-8")

    # Мокаем 3 input()
    mocker.patch(
        "builtins.input", side_effect=[coords_filename, input_filename, output_filename]
    )

    m_13_3_11()
    captured = capsys.readouterr()
    assert captured.out == expected_message
    result_map = output_path.read_text(encoding="utf-8")
    assert result_map == expected_output_map
    coords_path.unlink(missing_ok=True)
    map_path.unlink(missing_ok=True)
    output_path.unlink(missing_ok=True)
