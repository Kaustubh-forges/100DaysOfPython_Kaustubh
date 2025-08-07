# Caesar Cipher Project

#-------------------------

# Modules imported
from art import logo

# ASCII art for aesthetics
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# User inputs to start Caesar Cipher
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# User-defined function to shift message forward by a specific number
def encrypt(original_text,shift_amount):
    new_text=""

    # Loop for iterating through message + conditional statements that cause forward letter shifts
    for old_letter in original_text:
        if old_letter not in alphabet: # Keeps symbols and their positions unchanged
            new_text+=old_letter
        else:
            old_index = alphabet.index(old_letter) # Accessing index
            new_index = old_index + shift_amount # Replaces old letter with a new letter after shift
            new_index = new_index % len(alphabet)  # Modulo finds remainder for the new index
            # If the new index precedes the number of indexes available for use(is out of range), we use the remainder to get the shift value without encountering the out of range error
            # so, for example if new index is 27, but we only have 25 available, we get 2. So we can safely move from z(which is index 25) to b(which is index "27" even though it is really index 1)
            # if our new index is 22, then nothing will happen because 22%25 is still 22.
            new_text = new_text + alphabet[new_index]

    print(f"The encoded result is {new_text}.")

# User-defined function to shift message backwards by a specific number
def decrypt(original_text,shift_amount):
    new_text2=""
    for old_letter in original_text:
        if old_letter not in alphabet: # Keeps symbols and their positions unchanged
            new_text2+=old_letter
        else:
            old_index = alphabet.index(old_letter) # Accessing index
            new_index = old_index - shift_amount # Replaces old letter with a new letter after shift
            new_index = new_index % len(alphabet) # Modulo finds the remainder of the new index
            # If the new index precedes the number of indexes available for use(is out of range), we use the remainder to get the shift value without encountering the out of range error
            # so, for example if new index is 27, but we only have 25 available, we get 2. So we can safely move from z(which is index 25) to b(which is index "27" even though it is really index 1)
            # if our new index is 22, then nothing will happen because 22%25 is still 22.
            new_text2 += alphabet[new_index]
    print(f"The decoded result is {new_text2}.")

# User-defined function that calls other functions for encoding and decoding
def caesar(direction_to_go,original_text,shift_amount):
    if direction_to_go=="encode":
        encrypt(text,shift) # We can also use encrypt(original_text=text,shift_amount=shift)
    elif direction_to_go=="decode":
        decrypt(text,shift) # We can also use decrypt(original_text=text,shift_amount=shift)
    else:
        print("You entered an invalid option!")

# Calls the caesar function
caesar(direction,original_text=text,shift_amount=shift)

# Loop to enable continuation of Caesar Cipher
while True:
    check_again = input("Type 'yes' if you want to go again. Otherwise, type 'no'\n").lower()
    if check_again=="yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        # Calls function
        caesar(direction, original_text=text, shift_amount=shift)

    else:
        print("Well...I suppose we are done for the day.")
        break # Breaks out of the while loop and prevents further runs