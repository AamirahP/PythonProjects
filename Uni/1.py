#Dictionaries have key-value apris, seperated by a semi-colon

dict1 = {
    'key':42,
    'question': 'why are we here?',
    'is it true':True,
    5:'a number'
}

print(dict1['key'])
print(dict1)

dict1["car"] = 'red'
print(dict1)

del dict1['key']
print(dict1)

# Looping through keys and values
for key,value in dict1.items():
    print ('\nKey: ', key)
    print ('Value: ', value)


# has to be all str to run the following:

# for k in sorted(dict1.keys()):
#     print(k.title(), 'is on the list')

#Create a list of dictionaries with a loop

fruits = []

for x in range(30):
    new_fruit = {'type': 'apple', 'colour': 'green'}
    fruits.append(new_fruit)
    print(fruits)

# Update the first 5 elements of the list

for x in fruits[0:5]:
    if x['colour'] == 'green':
        x['colour'] = 'yellow'
        x['price'] = 1

for x in fruits[:7]:
    print(x)

print('...')

# Nested dictionaries 

users = {
    'asams123': {
        'fname': 'adam',
        'lname:': 'patel',
        'location': 'paris'
    },
    'sophia22': {
        'fname': 'sphia',
        'lname': 'the1st',
        'location': 'timbuk2'
    }
}