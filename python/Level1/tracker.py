from pathlib import Path
BASE_DIR = Path(__file__).parent
TASKS_FILE = BASE_DIR / "tasks.txt"


def menu():
    while True:
        option = input("1. Add task\n"
                       "2. Show tasks\n"
                       "3. Exit\n\n"
                       "Choose: ")
        if option == "1":
            add_task()
        elif option == "2":
            show_tasks()
        elif option == "3":
            print("EXITTING\n--------------------------------")
            break
        else:
            print("\nWrong input!\nCorrect form: 1 / 2 / 3\n")


def add_task():
    task = input("Task: ")
    with open(TASKS_FILE, "a") as f:
        f.write(task+"\n")
        return


def show_tasks():
    with open(TASKS_FILE, "r") as f:
        print(f.read())
        return


menu()
