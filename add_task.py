def add_task(items_list):
    task = " ".join(items_list)
    # Добавление проверки
    if not task:
        print("Введите текст задачи! Текст задачи не может быть пустым!")
        return
    print("task = " + task)
    with open("todo.txt", "a", encoding="utf-8") as f:
        f.write(f"[ ] {task}\n")
    print(f"Добавлено: [ ] {task}")