# Treasure Island Game Project

#---------------------------------

# ASCII art for aesthetics
print(r''' 
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Welcome message for users
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Get user input to start the game
direction=input("Enter the direction that you would like to take: left or right?\n")

# Conditional statements to decide outcome
if direction=="left" or direction=="Left":
    action1=input("You are facing two paths: A lake which you can swim across and a straight grassy road."
                  "Do you swim? Or do you walk?\n")
    if action1=="Swim"  or action1=="swim":
        print("Game over. You were swallowed alive by a Kraken.")
    else:
        action2=input("You are facing three colored doors: Yellow, Blue, and Red."
                      "Which one do you go through?\n")
        if action2=="Yellow" or action2=="yellow":
            print("Game over. You fell into a dark abyss that sent you straight to the Fields of Punishment!")
        elif action2=="red" or action2=="Red":
            print("Game over. You were send to a cave inhabited by a Dragon!")
        elif action2=="Blue" or action2=="blue":
            print('Congratulations! You have conquered this absurdly easy treasure hunt.'
                  'Your award is being able to eat and sleep since you are alive!')
        else:
            print("Wrong door color! You have been eliminated by our resident Centaur and his trusty arrow.")

else:
    print("Game over. You fell in a ditch and broke your most precious body part...hence suffering an excruciating and drawn out death!")

# Parting message for users
print("Thanks a lot for trying out this game!")