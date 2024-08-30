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

# file_to_delete = 'joke.txt'
# os.remove(file_to_delete)
# print(f'{file_to_delete} has been deleted')

#Merging files

file1_path = 'example.txt'
fil2_path = 'new_file.txt'
output = 'merged_file.txt'

with open(file1_path, 'r') as file1, open(fil2_path, 'r') as file2:
    data1 = file1.read()
    data2 = file2.read()

with open(output, 'w') as output_file:
    output_file.write(data1)
    output_file.write('\n')
    output_file.write(data2)

print('files have been merged successfully')


with open('data_file.txt', 'r') as file:
    #Read entire content of the file
    file_content = file.read()

print(file_content)

#Filter the file 

input_file = 'data_file.txt'
output_file = 'filtered_name.txt'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        name, surname, age = line.strip().split(',')
        if name.strip() != 'Alice':
            outfile.write(f'{name}, {surname}, {age} \n')


with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    first_line = True # A line to skip the first line 
    for line in infile:
        if first_line:
            output_file.write(line)
            first_line= False
            continue #Skip the first line
