# Hangman Project

#-----------------

# Specific components imported from modules
import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

# Imported ASCII art
print(logo)

# Random word chosen from imported list
chosen_word = random.choice(word_list)

# Constants
PLACEHOLDER = ""
DISPLAY = ""
# Function for length calculation of selected word
word_length = len(chosen_word)

# Loop for question creation
for position in range(word_length):
    PLACEHOLDER += "_"
print("Word to guess: " + PLACEHOLDER)

# List with empty-spaced elements + List matches the length of chosen word
display2 = [''] * len(chosen_word)

# List to store letters already matched
matched = []

# Number of available lifelines in game
lives = 6

# List to store unique(or previously unmatched) letters
unique_letters=[]

# Loop for game continuation until user guesses word or loses all lifelines
while chosen_word != DISPLAY and not lives == 0:
    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # Conditional statements for unique letter check + Adds unique letters to list
    if guess not in unique_letters:
        unique_letters.append(guess)
    else:
        print(f"The letter {guess} was already entered")

    # Loop matches user input to letters in the mystery word + Adds matched letters to list + Assigns position to correctly guessed letter
    for position2 in range(0, len(chosen_word)):
        if chosen_word[position2] == guess:
            matched.append(guess)
            display2[position2] = guess

        elif display2[position2] in matched:
            display2[position2] = display2[position2]

        else:
            display2[position2] = "_"

    # List gets converted to string
    DISPLAY = "".join(display2)

    # Prints current progress to check user's guess accuracy
    print(DISPLAY)

    # Conditional statements to print Hangman ASCII + Lifeline deduction, if needed
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives = lives - 1
        print(stages[lives])

    else:
        print(stages[lives])

# Prints win and loss statements
if lives == 0:
    print(f"The word was {chosen_word}!")
    print("**********You lose**********")
else:
    print("**********You Win**********")






