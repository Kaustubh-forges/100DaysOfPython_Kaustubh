
# Constants
max=0

# ASCII art for aesthetics
logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

# User input to get started
name=input("Enter your name: ").title()
price=int(input("Enter your bid: $"))

# Use of dictionary to store data
auction={}
auction[name]=price

ask_again=input("Are there any more bidders? Enter yes or no.\n").lower()

# Loop for additional user inputs
while ask_again=="yes":
    print("\n"*100)
    name = input("Enter your name: ").title()
    price = int(input("Enter your bid: $"))
    auction[name]=price
    ask_again = input("Are there any more bidders? Enter yes or no.\n").lower()

# Comparing stored bids in dictionary + Winner is declared
for key in auction:
    if auction[key]>max:
        max=auction[key]
for key in auction:
    if max==auction[key]:
        print(f"The winner is {key} with a bid of ${max}.")
