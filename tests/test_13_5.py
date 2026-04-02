import pytest
import csv
from pathlib import Path
from src.module_13 import (
    m_13_5_1,
    m_13_5_2,
    m_13_5_3,
    m_13_5_4,
    m_13_5_5,
    m_13_5_6,
    m_13_5_7,
    m_13_5_8,
    m_13_5_9,
)


# m_13_5_1: Создание CSV файла с данными о продажах
@pytest.mark.parametrize(
    "filename, expected_rows",
    [
        # Тест 1: Sample Input
        (
            "my_first_CSV.csv",
            [
                [
                    "order_id",
                    "customer_name",
                    "product",
                    "quantity",
                    "price",
                    "order_date",
                ],
                [1001, "Иван Петров", "Ноутбук", 1, 75000, "2024-01-15"],
                [1002, "Анна Сидорова", "Смартфон", 2, 45000, "2024-01-16"],
                [1003, "Сергей Иванов", "Наушники", 3, 5000, "2024-01-17"],
                [1004, "Мария Козлова", "Планшет", 1, 35000, "2024-01-18"],
                [1005, "Алексей Новиков", "Монитор", 2, 25000, "2024-01-19"],
            ],
        ),
    ],
)
def test_13_5_1(filename, expected_rows, mocker):
    mocker.patch("builtins.input", return_value=filename)

    m_13_5_1()

    file_path = Path(filename)
    assert file_path.exists()

    with file_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    expected = [[str(item) for item in row] for row in expected_rows]
    assert rows == expected

    file_path.unlink(missing_ok=True)


# m_13_5_2: Запись CSV файла с использованием DictWriter
def test_13_5_2(mocker):
    filename = "my_CSV_DictWriter.csv"
    mocker.patch("builtins.input", return_value=filename)

    m_13_5_2()

    file_path = Path(filename)
    assert file_path.exists()

    with file_path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        rows = list(reader)

    expected = [
        [
            "order_id",
            "customer_name",
            "product",
            "quantity",
            "price",
            "order_date",
        ],
        ["1001", "Иван Петров", "Ноутбук", "1", "75000", "2024-01-15"],
        ["1002", "Анна Сидорова", "Смартфон", "2", "45000", "2024-01-16"],
        ["1003", "Сергей Иванов", "Наушники", "3", "5000", "2024-01-17"],
        ["1004", "Мария Козлова", "Планшет", "1", "35000", "2024-01-18"],
        ["1005", "Алексей Новиков", "Монитор", "2", "25000", "2024-01-19"],
    ]

    assert rows == expected

    file_path.unlink(missing_ok=True)


# m_13_5_3: Анализ успеваемости студентов из CSV файла
@pytest.mark.parametrize(
    "input_filename, input_content, expected_output",
    [
        # Тест 1: Sample Input (несколько студентов с максимальным баллом)
        (
            "students1.csv",
            "id,name,age,grade\n"
            "1,Смирнов Игорь,20,90\n"
            "2,Попова Татьяна,21,90\n"
            "3,Кузнецов Сергей,22,85\n"
            "4,Новикова Юлия,19,90\n"
            "5,Морозов Артем,23,87\n",
            "Максимальный балл: 90\n"
            "Студенты: Новикова Юлия, Попова Татьяна, Смирнов Игорь\n",
        ),
        # Тест 2: Один студент с максимальным баллом
        (
            "single_top.csv",
            "id,name,age,grade\n"
            "1,Иванов Иван,20,70\n"
            "2,Петров Петр,21,95\n"
            "3,Сидоров Сергей,19,80\n",
            "Максимальный балл: 95\n" "Студенты: Петров Петр\n",
        ),
        # Тест 3: Все получили одинаковый балл
        (
            "all_equal.csv",
            "id,name,age,grade\n"
            "1,Борисов Алексей,20,100\n"
            "2,Андреев Андрей,21,100\n"
            "3,Васильева Анна,19,100\n",
            "Максимальный балл: 100\n"
            "Студенты: Андреев Андрей, Борисов Алексей, Васильева Анна\n",
        ),
        # Тест 4: Один студент в файле (пограничный случай)
        (
            "one_student.csv",
            "id,name,age,grade\n" "1,Егоров Егор,18,76\n",
            "Максимальный балл: 76\n" "Студенты: Егоров Егор\n",
        ),
        # Тест 5: Максимальный балл равен 0 (нижняя граница)
        (
            "zero_grade.csv",
            "id,name,age,grade\n" "1,Иванов Иван,20,0\n" "2,Петров Петр,21,0\n",
            "Максимальный балл: 0\n" "Студенты: Иванов Иван, Петров Петр\n",
        ),
    ],
)
def test_13_5_3(input_filename, input_content, expected_output, mocker, capsys):
    mocker.patch("builtins.input", return_value=input_filename)

    input_path = Path(".") / input_filename
    input_path.write_text(input_content, encoding="utf-8")

    m_13_5_3()

    captured = capsys.readouterr()
    assert captured.out == expected_output

    input_path.unlink(missing_ok=True)
