name = input("Name: ")
age = input("Age: ")

if age.isnumeric():
    age = int(age)
    if age < 18:
        print(f"{name}, you're a teenager and in 10 years you'll be {age+10}.")
    else:
        print(f"{name}, you're an adult and in 10 years you'll be {age+10}.")
else:
    print(f"{name} you haven't told me your age!")