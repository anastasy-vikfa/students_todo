
import os


def list_tasks(show_all=True):
    file_name = "ToDo.txt"
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        print("Список задач пуст.")
    else:
        print(" ВАШ СПИСОК ЗАДАЧ:")
        with open(file_name, "r", encoding="utf-8") as f:
            for number, line in enumerate(f, start=1):
                cleaned_line = line.strip()
                is_completed = cleaned_line.startswith("[x]")
                if not show_all and is_completed:
                    continue
                print(f"{number}. {cleaned_line}")
