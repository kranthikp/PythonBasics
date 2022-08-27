#what is a function?
"""
unit of code that can be resused through a program

each function can be called by itself
provides - modularity and code reusability

a function starts with 'def'
example def {function_name()}:
            ###
"""
#function defination
def addition():#function declaration
    a = -10.223
    b = 123
    print(a+b)

#function call
addition()

#getting user input
#python has input() buildin fucntion used to take user input
def multiply():#function declaration
    a = int(input("enter a number "))
    b = float(input("enter another number "))
    print(a*b)

multiply()
