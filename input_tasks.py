def save_task():
    task = input("Введите задачу: ")
    project = input("Проект: ")
    priority = input("Задайте приоритет (A, B или C): ")
    tag = input("Введите тег: ")

    line = f"({priority}) {task} @{project} +{tag}\n"
    with open("ToDo.txt","a",encoding="utf-8") as f:
        f.write(line)
        print("Задача сохранена") 
        print(line) 
        
save_task()