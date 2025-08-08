# Guess The Number Game Project

#--------------------------------

# Modules imported
import random
import art

# Function to generate a random number that has to be guessed
def random_winner():
    winning_number=random.randint(0,100)
    return winning_number

# Receives the number user needs to win
receiving_winner=random_winner()

# Function to compare user entered guess to correct number + Returns chaotic lists with results of comparison
def matching_numbers(num,receiving_winner):
    if num>receiving_winner:
        return ["Too High","Greater",True]
    elif num<receiving_winner:
        return ["Too Low","Lower",True]
    else:

        return [f"You got it! The answer was {num}","Correct",False]

# ASCII art for aesthetics
print(art.logo)

# Welcome message + Game starts
print("Welcome to the Number Guessing Game!")
print("You will be guessing a number between 1 and 100")
should_continue=True
level=input("Choose a difficulty method. Type 'easy' or 'hard': ").lower()

# User selects difficulty level(appropriate number of lifelines provided)
if level=="easy":
    chances=10
elif level=="hard":
    chances=5
else:
    chances=0


while should_continue and chances>0:
    print(f"You have {chances} chances left to guess the number.")
    chances-=1
    # User guesses a number
    guess=int(input("Guess your number: "))
    result=matching_numbers(guess,receiving_winner)
    # Checks if user guess is bigger than correct number
    if result[1]=="Greater":
        print(result[0])
        # Checks if user is out of lifelines
        if chances!=0:
            print("Guess again")
        else:
            print("Oops! You ran out of chances.")

    # Checks if user guess is smaller than correct number
    elif result[1]=="Lower":
        print(result[0])
        # Checks if user is out of lifelines
        if chances!=0:
            print("Guess again")
        else:
            print("Oops! You ran out of chances.")

    else:
        print(result[0])
        should_continue=result[2] # Gets True if program needs to continue, False if not

