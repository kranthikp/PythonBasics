#decision tree
"""
if age>18 =>> cast vote
otherwise not eligble

Comparision operators
< <= > >= == !=
"""
print(1<1)
print(1<=1)
print(1>1)
print(1>=1)
print(1==1)
print(1!=1)

"""
Control Statements
if elif and else
"""
name = input("Enter name ")
if name == "Kranthi":
    print("hello, nice to see you {} ".format(name))
print("Have a nice day")

fname = input("Enter name ")
if fname == "Kranthi":
    print("hello, nice to see you {} ".format(name))
elif fname == "panda":
    print("Hello, you are great")
elif fname == "kumar":
    print("good day!!")
elif fname != "kk":
    print("!!")
else:
    print("nice day")
