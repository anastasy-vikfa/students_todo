def save_task(items_list):
    task = " ".join(items_list)
    print("task = " + task)
    with open("todo.txt", "a", encoding="utf-8") as f:
        f.write(f"[ ] {task}\n")
    print(f"Добавлено: [ ] {task}")