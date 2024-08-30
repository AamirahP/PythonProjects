#append, write, merge, delete

import os


file_name = 'joke.txt'
with open(file_name, 'w') as file:
    file.write('why don\'t programmers like nature? \n')
          
#append to file content
#The orginial file will be modified

with open(file_name, 'a') as file:
    file.write('It\'s got too many bugs \n lol \n got eeeeeeem')


#Deleting

file_to_delete = 'joke.txt'
os.method(file_to_delete)