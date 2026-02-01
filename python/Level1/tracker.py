from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
TASKS_FILE = BASE_DIR / "tasks.txt"
task_number = 0


def menu():
    while True:
        option = input("WHAT TO DO\n"
                       "1. Add task\n"
                       "2. Show tasks\n"
                       "3. Mark task as done\n"
                       "4. Exit\n\n"
                       "Choose: ")
        if option == "1":
            add_task()
        elif option == "2":
            print("\n"+show_tasks()+"------------------------------\n")
        elif option == "3":
            if show_tasks() != "You have no tasks yet!\n":
                print("\n"+show_tasks())
                mark_done()
            else:
                print("\n"+show_tasks()+"------------------------------\n")
        elif option == "4":
            print("EXITTING\n--------------------------------")
            break
        else:
            print("\nWrong input!\nCorrect form: 1 / 2 / 3 / 4\n")


def add_task():
    global task_number
    task_number += 1
    task = input("Task: ")
    with open(TASKS_FILE, "a") as f:
        f.write(f"{task_number}. [ ] {task}\n")
        return


def show_tasks():
    with open(TASKS_FILE, "r") as f:
        x = f.read()
        if x == "":
            return "You have no tasks yet!\n"
        else:
            return x


def mark_done():
    mark_done_line_num = int(input("Mark done: ")) - 1
    whole_text = list()
    with open(TASKS_FILE, "r") as f:
        whole_text = f.readlines()
        if "[X]" in whole_text[mark_done_line_num]:
            print("\nTask already done\n")
            return
        else:
            whole_text[mark_done_line_num] = whole_text[mark_done_line_num].replace("[ ]", "[X]")
    with open(TASKS_FILE, "w") as f:
        for line in whole_text:
            f.write(line)
    print(show_tasks())



menu()
