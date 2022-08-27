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
#add()
#subtraction()
#multiply()
#divide()

operation = input("Please choose +, -, *, or / ")
if operation == '+':
    add()
elif operation == '-':
    subtraction()
elif operation == '*':
    multiply()
elif operation == '/':
    divide()
else:
    print("choose correct symbol")

