print ('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to treasure island. your mission is to find the treasure.")
step_1 = input("Would you like to go left(L) or right(R)? \n").lower()
if step_1 == "l":
    step_2 = input("Would you like to Swim(S) or Wait(W)? \n").lower()
    if step_2 == "w":
        step_3 = input("Choose a door: Red(R), Blue(B) or Yellow(Y)? \n").lower()
        if step_3 == "r":
            print("You have been burned by fire. Game Over!")
        elif step_3 == "b":
            print("Eaten by beasts. Game over!")
        elif step_3 == "y":
            print("Congratulations, you found the treasure. You win!")
        else:
            print("You lose, game over!")
    else:
        print("You have been attacked by a trout. Game Over!")
else:
    print("You fell into a hole. Game over!")