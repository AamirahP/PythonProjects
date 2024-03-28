print("Welcome to the tip calculator")
total = input("What was the total bill? £")
tip = input("How much tip would you like to give? 10,12 or 15 ")
people = input("How many people to split the bill? ")

if tip==10:
    total = (float(total) * 1.1)
if tip==12:
    total = (float(total) * 1.12)
if tip==15:
    total = (float(total) * 1.15)


total = (float(total) / int(people))

print(f"Each person should pay {total}")