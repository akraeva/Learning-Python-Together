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
            "2024-02-01;5;10;Cloudy;4.4\n",
        ),
        # Тест 3: Дробные значения температуры и скорости ветра
        (
            "decimal.csv",
            "decimal_result.csv",
            "date;temp_c;wind_kmh;condition\n" "2024-03-01;7.5;12.5;Rain\n",
            "date;temp_c;wind_kmh;condition;feels_like_c\n"
            "2024-03-01;7.5;12.5;Rain;6.8\n",
        ),
        # Тест 4: Отрицательная температура и сильный ветер
        (
            "cold.csv",
            "cold_result.csv",
            "date;temp_c;wind_kmh;condition\n" "2024-01-20;-20;40;Blizzard\n",
            "date;temp_c;wind_kmh;condition;feels_like_c\n"
            "2024-01-20;-20;40;Blizzard;-29.6\n",
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


# m_13_5_8: Расчет ИМТ
@pytest.mark.parametrize(
    "input_filename, output_filename, input_content, expected_content",
    [
        # Тест 1: Sample Input
        (
            "persons1.csv",
            "imt_persons1.csv",
            "name,height_cm,weight_kg\n"
            "Иван,180,75\n"
            "Анна,165,60\n"
            "Петр,190,110\n"
            "Мария,165,45\n",
            "name,height_cm,weight_kg,bmi,category\n"
            "Иван,180,75,23.1,Норма\n"
            "Анна,165,60,22.0,Норма\n"
            "Петр,190,110,30.5,Ожирение I степени\n"
            "Мария,165,45,16.5,Недостаточная (дефицит) масса тела\n",
        ),
        # Тест 2: Все категории ИМТ
        (
            "all_categories.csv",
            "all_categories_result.csv",
            "name,height_cm,weight_kg\n"
            "A,170,45\n"
            "B,170,50\n"
            "C,170,65\n"
            "D,170,80\n"
            "E,170,95\n"
            "F,170,110\n"
            "G,170,125\n",
            "name,height_cm,weight_kg,bmi,category\n"
            "A,170,45,15.6,Выраженный дефицит массы тела\n"
            "B,170,50,17.3,Недостаточная (дефицит) масса тела\n"
            "C,170,65,22.5,Норма\n"
            "D,170,80,27.7,Избыточная масса тела\n"
            "E,170,95,32.9,Ожирение I степени\n"
            "F,170,110,38.1,Ожирение II степени\n"
            "G,170,125,43.3,Ожирение III степени\n",
        ),
        # Тест 3: Дробные значения роста и веса
        (
            "decimal.csv",
            "decimal_result.csv",
            "name,height_cm,weight_kg\n" "Анна,165.5,58.7\n",
            "name,height_cm,weight_kg,bmi,category\n" "Анна,165.5,58.7,21.4,Норма\n",
        ),
        # Тест 4: Один человек
        (
            "single.csv",
            "single_result.csv",
            "name,height_cm,weight_kg\n" "Иван,180,81\n",
            "name,height_cm,weight_kg,bmi,category\n"
            "Иван,180,81,25.0,Избыточная масса тела\n",
        ),
        # Тест 5: Пустой файл
        (
            "empty.csv",
            "empty_result.csv",
            "name,height_cm,weight_kg\n",
            "name,height_cm,weight_kg,bmi,category\n",
        ),
    ],
)
def test_13_5_8(
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

    m_13_5_8()

    assert output_path.exists()
    assert output_path.read_text(encoding="utf-8") == expected_content

    input_path.unlink(missing_ok=True)
    output_path.unlink(missing_ok=True)


@pytest.mark.parametrize(
    (
        "input_filename",
        "output_filename",
        "input_content",
        "expected_content",
    ),
    [
        # Тест 1. Пример из условия
        (
            "analysis_test1.csv",
            "result_analysis_test1.csv",
            (
                "sample_id,Fe,Cr,Ni,Mo,C,Si,Mn,P,S,Cu\n"
                "ANALYSIS-001,68.5,18.2,8.9,0.1,0.08,0.75,1.2,0.045,0.03,0.15\n"
                "ANALYSIS-002,71.3,16.8,10.5,2.1,0.03,0.45,1.8,0.035,0.02,0.25\n"
                "ANALYSIS-003,71.0,17.5,0.4,0.1,0.10,0.4,0.6,0.035,0.025,0.15\n"
                "ANALYSIS-004,95.8,0.3,0.2,0.05,0.20,0.2,0.7,0.03,0.02,0.1\n"
                "ANALYSIS-005,96.5,0.4,0.3,0.08,0.45,0.3,0.6,0.025,0.015,0.08\n"
                "ANALYSIS-006,93.0,0.2,0.1,0.02,3.4,2.0,0.6,0.04,0.03,0.05\n"
                "ANALYSIS-007,93.5,0.3,0.2,0.03,3.6,2.4,0.7,0.035,0.025,0.06\n"
                "ANALYSIS-008,99.3,0.05,0.02,0.01,0.08,0.1,0.2,0.01,0.005,0.03\n"
            ),
            (
                "sample_id,Fe,Cr,Ni,Mo,C,Si,Mn,P,S,Cu,material_grade\n"
                "ANALYSIS-001,68.5,18.2,8.9,0.1,0.08,0.75,1.2,0.045,0.03,0.15,AISI 304 (08Х18Н10)\n"
                "ANALYSIS-002,71.3,16.8,10.5,2.1,0.03,0.45,1.8,0.035,0.02,0.25,AISI 316 (10Х17Н13М2)\n"
                "ANALYSIS-003,71.0,17.5,0.4,0.1,0.10,0.4,0.6,0.035,0.025,0.15,AISI 430 (12Х17)\n"
                "ANALYSIS-004,95.8,0.3,0.2,0.05,0.20,0.2,0.7,0.03,0.02,0.1,Неизвестный сплав\n"
                "ANALYSIS-005,96.5,0.4,0.3,0.08,0.45,0.3,0.6,0.025,0.015,0.08,Сталь 45\n"
                "ANALYSIS-006,93.0,0.2,0.1,0.02,3.4,2.0,0.6,0.04,0.03,0.05,СЧ20\n"
                "ANALYSIS-007,93.5,0.3,0.2,0.03,3.6,2.4,0.7,0.035,0.025,0.06,СЧ20\n"
                "ANALYSIS-008,99.3,0.05,0.02,0.01,0.08,0.1,0.2,0.01,0.005,0.03,Техническое железо\n"
            ),
        ),
        # Тест 2. Неизвестный сплав
        (
            "unknown.csv",
            "result_unknown.csv",
            (
                "sample_id,Fe,Cr,Ni,Mo,C,Si,Mn,P,S,Cu\n"
                "TEST-001,70.0,15.0,5.0,1.0,0.25,0.8,1.0,0.03,0.02,0.2\n"
            ),
            (
                "sample_id,Fe,Cr,Ni,Mo,C,Si,Mn,P,S,Cu,material_grade\n"
                "TEST-001,70.0,15.0,5.0,1.0,0.25,0.8,1.0,0.03,0.02,0.2,Неизвестный сплав\n"
            ),
        ),
        # Тест 3. Граничные значения AISI 304
        (
            "boundary.csv",
            "result_boundary.csv",
            (
                "sample_id,Fe,Cr,Ni,Mo,C,Si,Mn,P,S,Cu\n"
                "TEST-001,70.0,17,11,0.2,0.08,0.5,1.0,0.03,0.02,0.1\n"
            ),
            (
                "sample_id,Fe,Cr,Ni,Mo,C,Si,Mn,P,S,Cu,material_grade\n"
                "TEST-001,70.0,17,11,0.2,0.08,0.5,1.0,0.03,0.02,0.1,AISI 304 (08Х18Н10)\n"
            ),
        ),
        # Тест 4. Fe = 99%, но примесей слишком много
        (
            "iron_fail.csv",
            "result_iron_fail.csv",
            (
                "sample_id,Fe,Cr,Ni,Mo,C,Si,Mn,P,S,Cu\n"
                "TEST-001,99.0,0.3,0.2,0.1,0.1,0.1,0.1,0.05,0.03,0.02\n"
            ),
            (
                "sample_id,Fe,Cr,Ni,Mo,C,Si,Mn,P,S,Cu,material_grade\n"
                "TEST-001,99.0,0.3,0.2,0.1,0.1,0.1,0.1,0.05,0.03,0.02,Неизвестный сплав\n"
            ),
        ),
        # Тест 5. Пустой файл
        (
            "empty.csv",
            "result_empty.csv",
            "sample_id,Fe,Cr,Ni,Mo,C,Si,Mn,P,S,Cu\n",
            "sample_id,Fe,Cr,Ni,Mo,C,Si,Mn,P,S,Cu,material_grade\n",
        ),
    ],
)
def test_13_5_9(
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

    m_13_5_9()

    assert output_path.exists()
    assert output_path.read_text(encoding="utf-8") == expected_content

    input_path.unlink(missing_ok=True)
    output_path.unlink(missing_ok=True)
