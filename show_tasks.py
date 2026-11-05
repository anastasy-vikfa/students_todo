import os


def print_todo_list():
    file_name = "ToDo.txt"
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        print("Список задач пуст.")
    else:
        print(" ВАШ СПИСОК ЗАДАЧ:")
        with open(file_name, "r", encoding="utf-8") as f:
            for number, line in enumerate(f, start=1):
                print(f"{number}. {line.strip()}")
            
print_todo_list()