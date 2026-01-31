import json
import os
import sys
from datetime import datetime

FILE_NAME = "tasks.json"

# 1. Проверяем, есть ли файл, если нет — создаём пустой список
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump([], f)

# 2. Загружаем задачи в память
with open(FILE_NAME, "r", encoding="utf-8") as f:
    tasks = json.load(f)

# 3. Берём команду из аргументов
# пример: python back.py add "Buy groceries"
if len(sys.argv) > 2 and sys.argv[1] == "add":
    description = sys.argv[2]

    # создаём словарь задачи
    task = {
        "id": len(tasks) + 1,
        "description": description,
        "status": "todo",
        "createdAt": str(datetime.now()),
        "updatedAt": str(datetime.now())
    }

    # добавляем задачу в список
    tasks.append(task)

    # сохраняем обратно в файл
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

    print(f"Task added: {description} (ID: {task['id']})")
else:
    print("Использование: python back.py add \"Название задачи\"")
