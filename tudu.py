import sys
from show_tasks import print_todo_list
from input_tasks import save_task
from done import demadem

print("sys.argv: ",sys.argv)

# Проверяем, что нам передали команду
if len(sys.argv) < 2:
    print("Используйте: add, list или done")
    sys.exit()

command = sys.argv[1].lower()

# --- ДОБАВИТЬ ЗАДАЧУ ---
if command == "add":
    save_task(sys.argv[2:])

# --- ПОКАЗАТЬ СПИСОК ---
if command == "list":
    print_todo_list()

# --- ВЫПОЛНИТЬ ПО НОМЕРУ ---
if command == "done":
    demadem(sys.argv[2])
    

