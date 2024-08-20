current_num = 1

while (current_num <= 5):
    print(current_num)
    break

prompt = '\n Tell me something i will tell it back'
prompt += '\n Enter \'quict\' to end the loop'

message = input(prompt)

while message != 'quit':
    print(message)
    message = input(prompt)