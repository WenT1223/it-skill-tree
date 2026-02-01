task = input("Task: ")
tasks = open("python/Level1/tasks.txt", "a")
tasks.write(task+"\n")
tasks = open("python/Level1/tasks.txt", "r")

print(tasks.read())