from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
TASKS_FILE = BASE_DIR / "tasks.txt"


def menu():
    while True:
        option = input("WHAT TO DO\n"
                       "1. Add task\n"
                       "2. Show tasks\n"
                       "3. Mark task as done\n"
                       "4. Delete task\n"
                       "5. Toggle task done/undone\n"
                       "6. Exit\n\n"
                       "Choose: ")
        if option == "1":
            add_task()
        elif option == "2":
            x = read_tasks()
            if x:
                print(x)
            else:
                print("\nYou have no tasks!\n")
        elif option == "3":
            if read_tasks():
                mark_done()
            else:
                print("\nYou have no tasks!\n")
        elif option == "4":
            if read_tasks():
                delete_task()
            else:
                print("\nNo tasks to delete!\n")
        elif option == "5":
            if read_tasks():
                toggle_task()
            else:
                print("\nNo tasks to delete!\n")
        elif option == "6":
            print("EXITTING\n--------------------------------")
            break
        else:
            print("\nWrong input!\nCorrect form: 1 / 2 / 3 / 4 / 5 / 6\n")


def read_tasks():
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return f.read()
 

def write_out_tasks():
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        whole_text = f.readlines()
        for index, task in enumerate(whole_text):
            print(f"{index+1}. {task}", end="")
        return whole_text


def validate_input(the_input, whole_text_length):
    if the_input.isdigit():
        the_input = int(the_input) - 1
    else:
        print("Wrong input!\n")
        return None
    if the_input >= whole_text_length or the_input == -1:
        print("Wrong index!\n")
        return None
    return the_input


def add_task():
    task = input("Task: ")
    with open(TASKS_FILE, "a", encoding="utf-8") as f:
        f.write(f"[ ] {task}\n")


def mark_done():
    whole_text = write_out_tasks()
    line_index = input("Mark done: ")
    index = validate_input(line_index, len(whole_text))
    if index == None:
        return
    if whole_text[index].startswith("[X]"):
        print("\nTask already done\n")
        return
    else:
        whole_text[index] = whole_text[index].replace("[ ]", "[X]", 1)
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for line in whole_text:
            f.write(line)
            print(line, end="")


def delete_task():
    whole_text = write_out_tasks()
    line_index = input("Delete: ")
    index = validate_input(line_index, len(whole_text))
    if index == None:
        return
    whole_text.pop(index)
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for line in whole_text:
            f.write(line)
            print(line, end="")


def toggle_task():
    whole_text = write_out_tasks()
    line_index = input("Toggle: ")
    index = validate_input(line_index, len(whole_text))
    if index == None:
        return
    if whole_text[index].startswith("[X]"):
        whole_text[index] = whole_text[index].replace("[X]", "[ ]", 1)
    elif whole_text[index].startswith("[ ]"):
        whole_text[index] = whole_text[index].replace("[ ]", "[X]", 1)
    else:
        print("Invalid format in file")
        return
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for line in whole_text:
            f.write(line)
            print(line, end="")


menu()
