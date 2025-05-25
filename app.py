# Exercise 1

def fn2():
    print("I am function 2")

def fn1(func2):
    print("I am function 1")
    func2()

# fn1(fn2)

# Exercise 2
# def auth_checker(func1):
#     def wrapper():
#         print("Auth Checker Called")
#         func1()
    
#     return wrapper

# @auth_checker
# def access_dashboard():
#     print("Access Dashboard Called")

# access_dashboard("Talha")

# Exercise 3
def auth_checker_with_parameters(name, password):
    def auth_checker(func1):
        def wrapper():
            print("Auth Checker Called")
            if name == "Talha" and password == "Password":
                return func1()
            else:
                print("Invalid")
        return wrapper
        
    return auth_checker

username = "Talha"
pwd = "Password"
@auth_checker_with_parameters(username, pwd)
def access_dashboard():
    print("Access Dashboard Called ")

# access_dashboard()

# Exercise 4
names = ["Hamzah", "Ali", "Arham"]

# for (i, name) in enumerate(names, 1):
#     print(f"{i}. {name}")

# Exercise 5
# for i in range(1, 101):
#     print(i)

# Exercise 6
# for i in range(1, 11):
#     print(f"2 * {i} = {2 * i}")

# Exercise 7
import random

secret_number = random.randint(1, 100)

while True:
    my_guess = int(input("\nGuess the number: "))

    if my_guess > secret_number + 20:
        print("You Guessed Too High!")
    elif my_guess > secret_number + 10:
        print("You Guessed High!")
    elif my_guess > secret_number:
        print("You Guessed Little Bit High!")
    elif my_guess + 20 < secret_number:
        print("You Guessed Too Low!")
    elif my_guess + 10 < secret_number:
        print("You Guessed Low!")
    elif my_guess < secret_number:
        print("You Guessed Little Bit Low!")
    else:
        print("You Won!\n")
        break