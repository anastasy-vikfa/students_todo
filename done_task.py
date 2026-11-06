def done_task(item):
    num = int(item) - 1  # Получаем индекс строки (компьютер считает с 0)
    
    with open("todo.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    # Меняем [ ] на [x] в нужной строке
    lines[num] = lines[num].replace("[ ]", "[x]")
    
    with open("todo.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)
    
    print(f"Задача №{num + 1} выполнена!")