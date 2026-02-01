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
                       "5. Exit\n\n"
                       "Choose: ")
        if option == "1":
            add_task()
        elif option == "2":
            print("\n"+show_tasks()+"------------------------------\n")
        elif option == "3":
            if show_tasks() != "You have no tasks yet!\n":
                mark_done()
            else:
                print("\n"+show_tasks()+"------------------------------\n")
        elif option == "4":
            if show_tasks() != "You have no tasks yet!\n":
                mark_done()
            else:
                print("\n"+show_tasks()+"------------------------------\n")
        elif option == "5":
            print("EXITTING\n--------------------------------")
            break
        else:
            print("\nWrong input!\nCorrect form: 1 / 2 / 3 / 4\n")


def add_task():
    task = input("Task: ")
    with open(TASKS_FILE, "a", encoding="utf-8") as f:
        f.write(f"[ ] {task}\n")
        return


def show_tasks():
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        x = f.read()
        if x == "":
            no_tasks_yet = "You have no tasks yet!\n"
            return no_tasks_yet
        else:
            return x


def mark_done():
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        whole_text = f.readlines()
        for index, task in enumerate(whole_text):
            print(f"{index+1}. {task}", end="")
        mark_done_line_num = input("Mark done: ")
        if mark_done_line_num.isdigit():
            mark_done_line_num = int(mark_done_line_num) - 1
        else:
            print("Wrong input!\n")
            return
        if mark_done_line_num >= len(whole_text) or mark_done_line_num == -1:
            print("Wrong index!\n")
            return
        if whole_text[mark_done_line_num].startswith("[X]"):
            print("\nTask already done\n")
            return
        else:
            whole_text[mark_done_line_num] = whole_text[mark_done_line_num].replace("[ ]", "[X]", 1)
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for line in whole_text:
            f.write(line)
            print(line, end="")



menu()
