def done_task(item=None):
    # 1. Если не написали номер после done
    if not item:
        print("Выберите номер задачи!")
        return

    # Открываем файл и читаем все задачи
    with open("todo.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

    # 2. Если файл пустой (задач вообще нет)
    if len(lines) == 0:
        print("Задач нет!")
        return

    # 3. Если ввели число меньше 1 или больше, чем всего задач
    num = int(item)
    if num < 1 or num > len(lines):
        print(f"Выберите номер от 1 до {len(lines)}")
        return

    # Отмечаем задачу (вычитаем 1, так как Python считает с 0)
    lines[num - 1] = lines[num - 1].replace("[ ]", "[x]")

    # Сохраняем обратно в файл
    with open("todo.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f"Задача №{num} выполнена!")
