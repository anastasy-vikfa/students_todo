import sys
from list_tasks import list_tasks
from add_task import add_task
from done_task import done_task

print("sys.argv: ",sys.argv)

# Проверяем, что нам передали команду
if len(sys.argv) < 2:
    print("Используйте: add, list или done")
    sys.exit()

command = sys.argv[1].lower()

# --- ДОБАВИТЬ ЗАДАЧУ ---
if command == "add":
    add_task(sys.argv[2:])

# --- ПОКАЗАТЬ СПИСОК ---
if command == "list":
    list_tasks()

# --- ВЫПОЛНИТЬ ПО НОМЕРУ ---
if command == "done":
    done_task(sys.argv[2])
    

