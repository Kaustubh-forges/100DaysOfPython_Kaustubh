#Tip Calculator Project

#-------------------------

# Welcome message
print("Welcome to the Tip Calculator!")

# Gets input from users
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10%, 12%, or 15%? "))
people = int(input("How many people to split the bill? "))

# Calculation and presentation of solution
final_bill_for_each_person = round((((bill*(tip/100))+bill)/people),2)
# Using f-string to improve formatting and readability
print(f"Each person should pay: ${final_bill_for_each_person}")
