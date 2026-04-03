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


# m_13_5_4: Добавление нового студента в CSV файл
@pytest.mark.parametrize(
    "filename, input_content, student_data, expected_content",
    [
        # Тест 1: Sample Input
        (
            "students_data1.csv",
            "id,name,age,grade\n"
            "1,Смирнов Игорь,20,60\n"
            "2,Попова Татьяна,21,50\n"
            "3,Кузнецов Сергей,22,85\n"
            "4,Новикова Юлия,19,90\n"
            "5,Морозов Артем,23,59",
            "Иванова Анна,20,95",
            "id,name,age,grade\n"
            "1,Смирнов Игорь,20,60\n"
            "2,Попова Татьяна,21,50\n"
            "3,Кузнецов Сергей,22,85\n"
            "4,Новикова Юлия,19,90\n"
            "5,Морозов Артем,23,59\n"
            "6,Иванова Анна,20,95\n",
        ),
        # Тест 2: Один студент в файле
        (
            "single_student.csv",
            "id,name,age,grade\n" "1,Петров Иван,18,70\n",
            "Сидорова Анна,19,85",
            "id,name,age,grade\n" "1,Петров Иван,18,70\n" "2,Сидорова Анна,19,85\n",
        ),
        # Тест 3: Проверка удаления лишних пробелов
        (
            "spaces.csv",
            "id,name,age,grade\n" "1,Иванов Иван,20,80\n",
            "  Петров Петр  ,  21 ,  90  ",
            "id,name,age,grade\n" "1,Иванов Иван,20,80\n" "2,Петров Петр,21,90\n",
        ),
        # Тест 4: ID продолжается с максимального существующего
        (
            "large_id.csv",
            "id,name,age,grade\n" "10,Анна Иванова,20,75\n" "11,Игорь Петров,22,82",
            "Мария Смирнова,19,100",
            "id,name,age,grade\n"
            "10,Анна Иванова,20,75\n"
            "11,Игорь Петров,22,82\n"
            "12,Мария Смирнова,19,100\n",
        ),
        # Тест 5: Минимально возможный файл (только заголовок)
        (
            "empty.csv",
            "id,name,age,grade\n",
            "Первый Студент,18,60",
            "id,name,age,grade\n" "1,Первый Студент,18,60\n",
        ),
    ],
)
def test_13_5_4(
    filename,
    input_content,
    student_data,
    expected_content,
    mocker,
):
    mocker.patch(
        "builtins.input",
        side_effect=[filename, student_data],
    )

    file_path = Path(".") / filename
    file_path.write_text(input_content, encoding="utf-8")

    m_13_5_4()

    result = file_path.read_text(encoding="utf-8")
    assert result == expected_content

    file_path.unlink(missing_ok=True)


# m_13_5_5: Анализ успеваемости студентов из CSV файла II
@pytest.mark.parametrize(
    "input_filename, output_filename, input_content, expected_content",
    [
        # Тест 1: Sample Input
        (
            "students1.csv",
            "best_students1.csv",
            "id,name,age,grade\n"
            "1,Смирнов Игорь,20,60\n"
            "2,Попова Татьяна,21,50\n"
            "3,Кузнецов Сергей,22,85\n"
            "4,Новикова Юлия,19,90\n"
            "5,Морозов Артем,23,59\n",
            "id,name,age,grade\n" "3,Кузнецов Сергей,22,85\n" "4,Новикова Юлия,19,90\n",
        ),
        # Тест 2: Все студенты проходят фильтр
        (
            "all_pass.csv",
            "all_pass_result.csv",
            "id,name,age,grade\n"
            "1,Анна Иванова,18,61\n"
            "2,Игорь Смирнов,19,75\n"
            "3,Мария Петрова,20,100\n",
            "id,name,age,grade\n"
            "1,Анна Иванова,18,61\n"
            "2,Игорь Смирнов,19,75\n"
            "3,Мария Петрова,20,100\n",
        ),
        # Тест 3: Никто не проходит фильтр
        (
            "none_pass.csv",
            "none_pass_result.csv",
            "id,name,age,grade\n"
            "1,Иван Иванов,20,60\n"
            "2,Петр Петров,21,45\n"
            "3,Анна Смирнова,19,12\n",
            "id,name,age,grade\n",
        ),
        # Тест 4: Проверка строгого условия > 60
        (
            "border.csv",
            "border_result.csv",
            "id,name,age,grade\n"
            "1,Студент Один,20,60\n"
            "2,Студент Два,20,61\n"
            "3,Студент Три,20,60\n"
            "4,Студент Четыре,20,62\n",
            "id,name,age,grade\n" "2,Студент Два,20,61\n" "4,Студент Четыре,20,62\n",
        ),
        # Тест 5: Проверка сохранения порядка строк
        (
            "order.csv",
            "order_result.csv",
            "id,name,age,grade\n"
            "1,Первый,20,90\n"
            "2,Второй,21,61\n"
            "3,Третий,22,95\n"
            "4,Четвертый,23,62\n",
            "id,name,age,grade\n"
            "1,Первый,20,90\n"
            "2,Второй,21,61\n"
            "3,Третий,22,95\n"
            "4,Четвертый,23,62\n",
        ),
    ],
)
def test_13_5_5(
    input_filename,
    output_filename,
    input_content,
    expected_content,
    mocker,
):
    input_path = Path(".") / input_filename
    output_path = Path(".") / output_filename

    input_path.write_text(input_content, encoding="utf-8")

    mocker.patch(
        "builtins.input",
        side_effect=[input_filename, output_filename],
    )

    m_13_5_5()

    assert output_path.exists()
    assert output_path.read_text(encoding="utf-8") == expected_content

    input_path.unlink(missing_ok=True)
    output_path.unlink(missing_ok=True)


# m_13_5_6: Анализ успеваемости студентов из CSV файла III
@pytest.mark.parametrize(
    "input_filename, output_filename, input_content, expected_content",
    [
        # Тест 1: Sample Input
        (
            "students1.csv",
            "sort_students1.csv",
            "id,name,age,grade\n"
            "1,Смирнов Игорь,20,90\n"
            "2,Попова Татьяна,21,90\n"
            "3,Кузнецов Сергей,22,85\n"
            "4,Новикова Юлия,19,90\n"
            "5,Морозов Артем,23,87\n",
            "id,name,age,grade\n"
            "4,Новикова Юлия,19,90\n"
            "2,Попова Татьяна,21,90\n"
            "1,Смирнов Игорь,20,90\n"
            "5,Морозов Артем,23,87\n"
            "3,Кузнецов Сергей,22,85\n",
        ),
        # Тест 2: Все оценки разные
        (
            "different.csv",
            "different_result.csv",
            "id,name,age,grade\n"
            "1,Анна,20,60\n"
            "2,Борис,21,95\n"
            "3,Виктор,22,75\n"
            "4,Галина,23,82\n",
            "id,name,age,grade\n"
            "2,Борис,21,95\n"
            "4,Галина,23,82\n"
            "3,Виктор,22,75\n"
            "1,Анна,20,60\n",
        ),
        # Тест 3: Все оценки одинаковые (сортировка только по имени)
        (
            "same_grade.csv",
            "same_grade_result.csv",
            "id,name,age,grade\n"
            "1,Яков,20,80\n"
            "2,Анна,21,80\n"
            "3,Борис,22,80\n"
            "4,Виктор,23,80\n",
            "id,name,age,grade\n"
            "2,Анна,21,80\n"
            "3,Борис,22,80\n"
            "4,Виктор,23,80\n"
            "1,Яков,20,80\n",
        ),
        # Тест 4: Один студент
        (
            "single.csv",
            "single_result.csv",
            "id,name,age,grade\n" "1,Иван Иванов,20,100\n",
            "id,name,age,grade\n" "1,Иван Иванов,20,100\n",
        ),
        # Тест 5: Смешанный случай
        (
            "mixed.csv",
            "mixed_result.csv",
            "id,name,age,grade\n"
            "1,Олег,20,70\n"
            "2,Анна,21,90\n"
            "3,Борис,22,90\n"
            "4,Глеб,23,70\n"
            "5,Виктор,24,100\n"
            "6,Алексей,19,70\n",
            "id,name,age,grade\n"
            "5,Виктор,24,100\n"
            "2,Анна,21,90\n"
            "3,Борис,22,90\n"
            "6,Алексей,19,70\n"
            "4,Глеб,23,70\n"
            "1,Олег,20,70\n",
        ),
    ],
)
def test_13_5_6(
    input_filename,
    output_filename,
    input_content,
    expected_content,
    mocker,
):
    input_path = Path(".") / input_filename
    output_path = Path(".") / output_filename

    input_path.write_text(input_content, encoding="utf-8")

    mocker.patch(
        "builtins.input",
        side_effect=[input_filename, output_filename],
    )

    m_13_5_6()

    assert output_path.exists()
    assert output_path.read_text(encoding="utf-8") == expected_content

    input_path.unlink(missing_ok=True)
    output_path.unlink(missing_ok=True)


# m_13_5_7: Расчет ощущаемой температуры
@pytest.mark.parametrize(
    "input_filename, output_filename, input_content, expected_content",
    [
        # Тест 1: Sample Input
        (
            "weather1.csv",
            "t_weather1.csv",
            "date;temp_c;wind_kmh;condition\n"
            "2024-01-10;0;20;Windy\n"
            "2024-01-11;-10;5;Cold\n"
            "2024-01-12;20;3;Warm\n"
            "2024-01-13;25;0;Hot\n",
            "date;temp_c;wind_kmh;condition;feels_like_c\n"
            "2024-01-10;0;20;Windy;-2.8\n"
            "2024-01-11;-10;5;Cold;-10.3\n"
            "2024-01-12;20;3;Warm;22.0\n"
            "2024-01-13;25;0;Hot;28.7\n",
        ),
        # Тест 2: Один день
        (
            "single.csv",
            "single_result.csv",
            "date;temp_c;wind_kmh;condition\n" "2024-02-01;5;10;Cloudy\n",
            "date;temp_c;wind_kmh;condition;feels_like_c\n"
            "2024-02-01;5;10;Cloudy;2.2\n",
        ),
        # Тест 3: Дробные значения температуры и скорости ветра
        (
            "decimal.csv",
            "decimal_result.csv",
            "date;temp_c;wind_kmh;condition\n" "2024-03-01;7.5;12.5;Rain\n",
            "date;temp_c;wind_kmh;condition;feels_like_c\n"
            "2024-03-01;7.5;12.5;Rain;1.7\n",
        ),
        # Тест 4: Отрицательная температура и сильный ветер
        (
            "cold.csv",
            "cold_result.csv",
            "date;temp_c;wind_kmh;condition\n" "2024-01-20;-20;40;Blizzard\n",
            "date;temp_c;wind_kmh;condition;feels_like_c\n"
            "2024-01-20;-20;40;Blizzard;-29.5\n",
        ),
        # Тест 5: Пустой файл (только заголовок)
        (
            "empty.csv",
            "empty_result.csv",
            "date;temp_c;wind_kmh;condition\n",
            "date;temp_c;wind_kmh;condition;feels_like_c\n",
        ),
    ],
)
def test_13_5_7(
    input_filename,
    output_filename,
    input_content,
    expected_content,
    mocker,
):
    input_path = Path(".") / input_filename
    output_path = Path(".") / output_filename

    input_path.write_text(input_content, encoding="utf-8")

    mocker.patch(
        "builtins.input",
        side_effect=[input_filename, output_filename],
    )

    m_13_5_7()

    assert output_path.exists()
    assert output_path.read_text(encoding="utf-8") == expected_content

    input_path.unlink(missing_ok=True)
    output_path.unlink(missing_ok=True)
