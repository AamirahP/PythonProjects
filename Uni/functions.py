# user defined functions 

def say_hello(usr_name, age):
    print ("hello", usr_name)
    print("you are ", str(age), "years old")
    """
    some descripton of my funciton
    
    """
# if yuo dont define the parameters of the function there will be an error
say_hello('kevin', 33)

msg = input("is this correct?")

# Returning the data to code, middle argument optional

def get_formatted_name(fname, lname, mname = ''):
    if mname:
        full = fname + ' ' + mname + ' ' + lname
    else:
        full = fname + ' ' + lname
    return full.title()

person1= get_formatted_name('sarah', 'parker', 'jessica')
person2 = get_formatted_name("brad", "pritt")
print(person1)
print(person2)