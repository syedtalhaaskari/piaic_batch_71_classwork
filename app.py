# Exercise 1

def fn2():
    print("I am function 2")

def fn1(func2):
    print("I am function 1")
    func2()

# fn1(fn2)

# Exercise 2
def auth_checker(func1):
    def wrapper():
        print("Auth Checker Called")
        func1()
    
    return wrapper

@auth_checker
def access_dashboard():
    print("Access Dashboard Called")

access_dashboard("Talha")
