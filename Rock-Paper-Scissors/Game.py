# Rock, Paper, Scissor Game Project

#---------------------------------------

# Modules imported
import random

# ASCII art for pictorial representation
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# User input to get game started
user_input=int(input("Enter 0 for rock, 1 for paper, and 2 for scissors!\n"))

# Conditional branches if user chooses "rock"
if user_input==0:
    computer_choice=random.randint(0,2) # randint equips system to make a random play
    if computer_choice==0:
       print(f"You chose:"
             f""
             f" "
             f"{rock}\n")
       print(f"The computer chose:"
             f""
             f""
             f"{rock}\n")
       print("It's a draw! Atleast your luck is not completely screwed! ")

    elif computer_choice==1:
       print(f"You chose:"
             f""
             f" "
             f"{rock}\n")
       print(f"The computer chose:"
             f""
             f""
             f"{paper}\n")

       print("You lose! Is your luck really that bad?")

    else:
        print(f"You chose:"
              f""
              f" "
              f"{rock}\n")
        print(f"The computer chose:"
              f""
              f""
              f"{scissors}\n")

        print("You win! You better hope this luck works in other areas of your life!")

# Conditional branches if user chooses "paper"
elif user_input == 1:
    computer_choice = random.randint(0, 2) # randint equips system to make a random play
    if computer_choice == 0:
        print(f"You chose:"
              f""
              f" "
              f"{paper}\n")
        print(f"The computer chose:"
              f""
              f""
              f"{rock}\n")
        print("You win! You better hope this luck works in other areas of your life! ")

    elif computer_choice == 1:
        print(f"You chose:"
              f""
              f" "
              f"{paper}\n")
        print(f"The computer chose:"
              f""
              f""
              f"{paper}\n")

        print("It's a draw! Atleast your luck is not completely screwed!")

    else:
        print(f"You chose:"
              f""
              f" "
              f"{paper}\n")
        print(f"The computer chose:"
              f""
              f""
              f"{scissors}\n")

        print("You lose! Is your luck really that bad?")

# Conditional branches if user chooses "paper"
elif user_input == 2:
    computer_choice = random.randint(0, 2) # randint equips system to make a random play
    if computer_choice == 0:
        print(f"You chose:"
              f""
              f" "
              f"{scissors}\n")
        print(f"The computer chose:"
              f""
              f""
              f"{rock}\n")
        print("You lose! Is your luck really that bad? ")

    elif computer_choice == 1:
        print(f"You chose:"
              f""
              f" "
              f"{scissors}\n")
        print(f"The computer chose:"
              f""
              f""
              f"{paper}\n")

        print("You win! You better hope this luck works in other areas of your life! ")

    else:
        print(f"You chose:"
              f""
              f" "
              f"{scissors}\n")
        print(f"The computer chose:"
              f""
              f""
              f"{scissors}\n")

        print("It's a draw! Atleast your luck is not completely screwed!")