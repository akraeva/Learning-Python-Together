from pathlib import Path


def t_len(title, base=28):
    """Вычисляет длину почерка заголовка для docs"""
    length = len(title.strip())
    return (length // base + 1) * base


def new_module(module, name):
    """Создаёт файлы для нового учебного модуля"""
    data = {
        "module_file": {
            "name": f"src/module_{module}.py",
            "title": "# Stepick.org — Learning Python Together",
            "symbol": "",
            "content": f"# {module}. {name}\n\n",
            "message": "✅ Создан файл модуля: ",
        },
        "docs_file": {
            "name": f"docs/modules/module_{module}.rst",
            "title": f"Модуль {module}: {name}\n",
            "symbol": "=",
            "content": (
                f"\nРешения задач из Модуля {module} «{name}» курса Learning Python Together.\n\n"
                ".. contents::\n   :local:\n   :depth: 2\n   :backlinks: top\n\n\n"
                "Тесты к модулю\n----------------------------\n\n"
                f"   `Тесты к Модулю {module} <tests_{module}.html>`__ "
            ),
            "message": "✅ Создан файл доков: ",
        },
        "tests_doc_file": {
            "name": f"docs/modules/tests_{module}.rst",
            "title": f"Тесты к Модулю {module}: {name}\n",
            "symbol": "=",
            "content": "\n.. contents::\n    :local:\n",
            "message": "✅ Создан файл доков тестов: ",
        },
    }

    for _, file in data.items():
        filename = file["name"]
        path = Path(filename)
        if not path.exists():
            title = file["title"] + file["symbol"] * t_len(file["title"])
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"{title}\n")
                f.write(file["content"])
                print(f"{file["message"]} {filename}")


def append_structure(module, step, name, count):
    "Генерирует структуру для решения задач главы модуля"
    filename = f"src/module_{module}.py"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n# === {module}.{step} {name} ===\n\n")
        for i in range(1, count + 1):
            f.write(
                f'''
def m_{module}_{step}_{i}():
    """
    ...
    {"-" * 37}
    ...
    """
    pass


'''
            )
    print(f"✅ Структура добавлена в {filename}")
    return True


def append_docs(module, step, name, count):
    "Генерирует содержимое доков"
    filename = f"docs/modules/module_{module}.rst"
    with open(filename, "a", encoding="utf-8") as f:
        title = f"\n\n{name} ({module}.{step})"
        f.write(f"{title}\n{'-' * t_len(title)}\n")
        for i in range(1, count + 1):
            line = f".. autofunction:: src.module_{module}.m_{module}_{step}_{i}()\n"
            f.write(line)
    print(f"✅ Описание добавлено в {filename}")
    return True


def create_test_file(module, step, count):
    """Создаёт файл тестов с импортами"""
    filename = f"tests/test_{module}_{step}.py"

    imports = ",\n".join([f"    m_{module}_{step}_{i}" for i in range(1, count + 1)])
    content = f"import pytest\nfrom src.module_{module} import (\n{imports}\n)"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Создан файл тестов: {filename} ({count} импортов)")
    return True


def update_tests_docs(module, step, name):
    """Обновляет страницу доков с тестами к модулю"""
    filename = f"docs/modules/tests_{module}.rst"

    title = f"{name} ({module}.{step})"
    section_content = (
        f"\n{title}\n{"-" * t_len(title)}\n\n"
        f"Файл: ``tests/test_{module}_{step}.py``\n\n"
        f".. literalinclude:: ../../tests/test_{module}_{step}.py\n"
        "    :language: python\n    :linenos:\n\n"
    )
    with open(filename, "a", encoding="utf-8") as f:
        f.write(section_content)

    print(f"✅ Добавлена секция {name} ({module}.{step})")
    return True


def main():
    module = int(input("Номер модуля: "))
    step = int(input("Номер шага: "))
    count = int(input("Количество задач: "))
    name = input("Название главы: ")

    filename = f"src/module_{module}.py"
    path = Path(filename)
    if not path.exists():
        module_name = input("Название модуля: ")
        new_module(module, module_name)

    success = [
        append_structure(module, step, name, count),
        append_docs(module, step, name, count),
        create_test_file(module, step, count),
        update_tests_docs(module, step, name),
    ]

    if all(success):
        print("\n🎉 Готово!")
    else:
        print("\n❌ Ошибки при генерации!")


if __name__ == "__main__":
    main()
