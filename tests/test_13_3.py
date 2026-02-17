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
