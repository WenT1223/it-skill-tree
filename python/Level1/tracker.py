def menu():
    option = input("1. Add task\n2. Show tasks\n3. Exit\n\nChoose: ")
    if option == "1":
        add_task()
    elif option == "2":
        show_tasks()
    elif option == "3":
        quit()
    else:
        print("\nWrong input!\nCorrect form: 1 / 2 / 3\n")
        menu()


def add_task():
    task = input("Task: ")
    with open("C:/Users/frict/Documents/VSCODE/it-skill-tree/python/Level1/tasks.txt", "a") as f:
        f.write(task+"\n")
        menu()


def show_tasks():
    with open("C:/Users/frict/Documents/VSCODE/it-skill-tree/python/Level1/tasks.txt", "r") as f:
        print(f.read())
        menu()


menu()