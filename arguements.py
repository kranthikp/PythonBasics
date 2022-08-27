def user_info(name, age, city):
    """This function print name, age and city form an argument
provided to the function."""

    print("{} is {} years old, from {}".format(name, age, city))
#args - arguments
user_info("James", 22, "Delhi")
#user_info(22, "Delhi") throws syntax error for missing arg

#kargs - keyword arguments
user_info(age=15, name= "ram", city="dwaraka")

""" Understanding *args
    contents: allow for unlimited variables to be passed
    into a function without defining them ahead of time
    def add(*args):
        print(sum(args))
    add(2,3,4)
    add(2,3,4,6,8,91)
    
    Understanding **kwargs
    contents: allow for unlimited variables to be passed
    into a function without defining them ahead of time
    def add(**kargs):
        print(**kwargs)

    Combining args types **kwargs
    all three args type cam be used in a single funciton.
    This must ne used in order: formal positional args, *arg," **kwargs
    def app(fname, lname, email, company, *args, **kargs):
        print("{} {} work at {}. Her email os {}.".format(fname, lname, company, email))
    
    app("kranthi", "panda", "kk@rgt.com", "test.org", 75000, hire_date= "sep 2021")
    """