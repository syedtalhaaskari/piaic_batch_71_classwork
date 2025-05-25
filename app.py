# Exercise 1

def fn2():
    print("I am function 2")

def fn1(func2):
    print("I am function 1")
    func2()

fn1(fn2)