import os
from pathlib import Path


def append_structure(module, step, name, count):
    "Генерирует структуру для решения задач главы модуля"
    filename = f"../src/module_{module}.py"
    path = Path(filename)

    if not path.exists():
        print(f"❌ {filename} не найден!")
        return False

    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n\n# === {module}.{step} {name} ===\n")
        for i in range(1, count + 1):
            f.write(
                f'''
    def m_{module}_{step}_{i}():
    """
    ...
    {"-"*37}
    ...
    """
    pass

'''
            )
    print(f"✅ Структура добавлена в {filename}")
    return True


def append_docs(module, step, name, count):
    "Генерирует содержимое доков"
    filename = f"../docs/modules/module_{module}.rst"
    path = Path(filename)

    if not path.exists():
        print(f"❌ {filename} не найден!")
        return False

    with open(filename, "a", encoding="utf-8") as f:
        title = f"\n\n{name} ({module}.{step})"
        length = max(26, (len(title) // 25 + 1) * 26)
        f.write(f"{title}\n{'-' * length}\n")
        for i in range(1, count + 1):
            line = f".. autofunction:: src.module_{module}.m_{module}_{step}_{i}()\n"
            f.write(line)

    print(f"✅ Описание добавлено в {filename}")
    return True


def create_test_file(module, step, count):
    """Создаёт файл тестов с импортами"""
    filename = f"../tests/test_{module}_{step}.py"
    path = Path(filename)

    if path.exists() and path.stat().st_size > 0:
        print(f"⚠️ {filename} уже существует")
        return True

    imports = ",\n".join([f"    m_{module}_{step}_{i}" for i in range(1, count + 1)])
    content = f"import pytest\nfrom src.module_{module} import (\n{imports}\n)"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Создан файл тестов: {filename} ({count} импортов)")
    return True


def create_or_update_tests_docs(module, step, name):
    """Создаёт/обновляет страницу доков с тестами к модулю"""
    filename = f"../docs/modules/tests_{module}.rst"
    path = Path(filename)

    if not path.exists():
        title = f"Тесты к Модулю {module}: НАЗВАНИЕ"
        length = 28
        header_content = f"""
Тесты к Модулю {module}: {name}
{"=" * length}

.. contents::
    :local:

"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(header_content)

        print(f"✅ Создан файл: {filename}")
    title = f"{name} ({module}.{step})"
    length = max(28, (len(title) // 28 + 1) * 28)
    section_content = f"""
{title}
{"-" * 28}

Файл: ``tests/test_{module}_{step}.py``

.. literalinclude:: ../../tests/test_{module}_{step}.py
    :language: python
    :linenos:

"""

    with open(filename, "a", encoding="utf-8") as f:
        f.write(section_content)

    print(f"✅ Добавлена секция {name} ({module}.{step})")
    return True


def main():
    module = int(input("Номер модуля: "))
    step = int(input("Номер шага: "))
    count = int(input("Количество задач: "))
    name = input("Название главы: ")

    success = [
        append_structure(module, step, name, count),
        create_test_file(module, step, count),
        append_docs(module, step, name, count),
        create_or_update_tests_docs(module, step, name),
    ]

    if all(success):
        print("\n🎉 Готово!")
    else:
        print("\n❌ Ошибки при генерации!")


if __name__ == "__main__":
    main()
