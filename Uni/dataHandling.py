# Reading, writing, deleting, closing and merging text files 

# Open Function 

file = open('my_file1.txt', 'w') #First argument file name or path + file name , 
# and second argument is 'w' - write a new file 

file.write('Hello MKU')
file.close()

file2 = open('/home/aamirah.patel/Documents/PythonProjects/my_file2.txt', 'w') #First argument file name or path + file name , 
# and second argument is 'w' - write a new file 

file2.write('Hello MKU, hi')
file2.close()

#option 2 - with the 'try' statement:

file3 = open('my_file3.txt', 'w')
try: 
    file3.write('hello world')
finally:
    file.close()

#option 3 - the use of 'with' keyword

with open('my_file4.txt', 'x') as file4:
    file4.write('hello 4')

