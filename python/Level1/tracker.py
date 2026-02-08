from pathlib import Path
import json
BASE_DIR = Path(__file__).resolve().parent
TASKS_FILE_TXT = BASE_DIR / "tasks.txt"
TASKS_FILE_JSON = BASE_DIR / "tasks.json"


def menu():
    options = [add_task, print_tasks, mark_done, delete_task, toggle_task]
    while True:
        tasks = load_tasks()
        option_pick = input("WHAT TO DO\n"
                       "1. Add task\n"
                       "2. Show tasks\n"
                       "3. Mark task as done\n"
                       "4. Delete task\n"
                       "5. Toggle task done/undone\n"
                       "6. Exit\n\n"
                       "Choose: ")
        if option_pick == "6":
            break
        elif option_pick.isdigit() and 1 <= int(option_pick) <= len(options):
            options[int(option_pick)-1](tasks)
        else:
            print("\nWrong input!\nCorrect form: 1 / 2 / 3 / 4 / 5 / 6\n")


def tasks_txt_to_json():
    with open(TASKS_FILE_TXT, "r", encoding="utf-8") as f:
        tasks_list = f.readlines()
    tasks = []
    for line in tasks_list:
        if line.startswith("[ ]"):
            done = False
            line = line.replace("[ ] ", "")
        elif line.startswith("[X]"):
            done = True
            line = line.replace("[X] ", "")
        else:
            print("Txt file corrupted")
            return
        tasks.append({
            "text": line.strip(),
            "done": done
        })
    save_tasks(tasks)
    old_file = BASE_DIR / "tasks_old.txt"
    if old_file.exists():
        old_file.unlink()
    TASKS_FILE_TXT.rename(old_file)
    print("Migration complete.")
    

def load_tasks():
    if not TASKS_FILE_JSON.exists():
        return []
    elif TASKS_FILE_JSON.stat().st_size == 0:
        return []
    else:
        with open(TASKS_FILE_JSON, "r", encoding="utf-8") as f:
            return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE_JSON, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks):
    text = input("Task: ").strip()
    if not text:
        print("Task cannot be empty")
        return
    tasks.append({
        "text": text,
        "done": False
    })
    save_tasks(tasks)


def print_tasks(tasks):
    if not tasks:
        print("No tasks")
        return
    for i, value in enumerate(tasks):
        done = "[X]" if value["done"] else "[ ]"
        print(f"{i+1}. {done} {value['text']}")


def mark_done(tasks):
    if not tasks:
        print("No tasks")
        return
    print_tasks(tasks)
    mark_line = input("Mark done: ")
    index = validate_input(mark_line, len(tasks))
    if index is None:
        return
    elif tasks[index]["done"]:
        print("Task already done")
        return
    tasks[index]["done"] = True
    save_tasks(tasks)
    print_tasks(tasks)


def toggle_task(tasks):
    if not tasks:
        print("No tasks")
        return
    print_tasks(tasks)
    mark_line = input("Toggle done/undone: ")
    index = validate_input(mark_line, len(tasks))
    if index is None:
        return
    tasks[index]["done"] = not tasks[index]["done"]
    save_tasks(tasks)
    print_tasks(tasks)


def validate_input(the_input, len_tasks):
    if the_input.isdigit():
        the_input = int(the_input) - 1
        if not (0 <= the_input < len_tasks):
            print("Wrong index!\n")
            return None
        return the_input
    else:
        print("Wrong input!\n")
        return None


def delete_task(tasks):
    if not tasks:
        print("No tasks")
        return
    print_tasks(tasks)
    mark_line = input("Delete: ")
    index = validate_input(mark_line, len(tasks))
    if index is None:
        return
    tasks.pop(index)
    save_tasks(tasks)
    print_tasks(tasks)


if TASKS_FILE_TXT.exists() and (not TASKS_FILE_JSON.exists() or TASKS_FILE_JSON.stat().st_size == 0):
    tasks_txt_to_json()

menu()
