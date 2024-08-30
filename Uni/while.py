current_num = 1

# while (current_num <= 5):
#     print(current_num)
#     break

prompt = '\n Tell me something i will tell it back'
prompt += '\n Enter \'quit\' to end the loop '

message = input(prompt)

while message != 'quit':
    print(message)
    message = input(prompt)


while current_num <10:
    current_num += 1

    if current_num % 2 == 0:
        continue
    print(current_num) 


# Removing from a list e.g. a list called dishes
# dishes.remove('pizza')

# CReate a while loop with function 

def get_formatted_name(fname, lname):

    full = fname + '' + lname
    return full.title()

while True:
    print('\n PLease tell me your name')
    print ('enter \'q\' at any time to quit: \n')

    fname = input('First name: ')
    if fname == 'q':
        break
    lname = input ('Last name: ')
    if lname == 'q':
        break 

    formatted_name = get_formatted_name(fname, lname)
    print('\n Hellno, fo')

