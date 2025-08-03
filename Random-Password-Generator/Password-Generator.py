# Random Password Generator Project

#-------------------------------------

# Modules imported
import random

# Lists used for password creation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message
print("Welcome to the PyPassword Generator!")

# User enters password specifications
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

Password_in_list_form=[] # List will hold password characters

# Looping through the lists above + Randomly picking elements from lists + Appending elements to a new list
for letter in range(0,nr_letters):
    random_letter=random.choice(letters)
    Password_in_list_form.append(random_letter)
for symbol in range(0,nr_symbols):
    random_symbol=random.choice(symbols)
    Password_in_list_form.append(random_symbol)
for number in range(0,nr_numbers):
    random_number=random.choice(numbers)
    Password_in_list_form.append(random_number)

random.shuffle(Password_in_list_form) # Shuffling the list with password in a random order

# Loop through list for better solution format (normal text)
print("Your generated password: ",end='')
for individual_element in Password_in_list_form:
    print(individual_element,end='')