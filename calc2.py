##using loop in calc2
on = True
def add():
    a = float(input("enter a num"))
    b = float(input("enter another num"))
    print(a+b)

def subtraction():
    a = float(input("enter a num"))
    b = float(input("enter another num"))
    print(a-b)

def multiply():
    a = float(input("enter a num"))
    b = float(input("enter another num"))
    print(a*b)

def divide():
    a = float(input("enter a num"))
    b = float(input("enter another num"))
    print(a/b)

while on:
    operation = input("Please choose +, -, *, /, or q ")
    if operation == '+':
        add()
    elif operation == '-':
        subtraction()
    elif operation == '*':
        multiply()
    elif operation == '/':
        divide()
    elif operation == 'q':
        on = False
    else:
        print("choose correct symbol")

