# Coffee machine project

#------------------------

# Coffee machine components in dictionary form
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# initial ingredients and their capacity
Water_initially=300
Milk_initially=200
Coffee_initially=100
money_initially=0

# Converts the number of coins into dollar amount using math + Return sum of total inn dollars
def conversion_of_money(quarters,dimes,nickles,pennies):
    quarters_in_dollars=quarters*0.25
    dimes_in_dollars=dimes*0.10
    nickes_in_dollars=nickles*0.05
    pennies_in_dollars=pennies*0.01

    return quarters_in_dollars+dimes_in_dollars+nickes_in_dollars+pennies_in_dollars

# Subtracts the money given with the cost of beverage ordered
def change_given_back(money,drink,menu):
    change=money-menu[drink]["cost"]
    return change


def ask_input():
    ask_user=input("What would you like? (espresso/latte/cappuccino): ").lower()
    return ask_user

should_continue=True

while should_continue:
    guess=ask_input()
    if guess=="report":
        print(f"Water: {Water_initially}ml\nMilk: {Milk_initially}ml\nCoffee: {Coffee_initially}g\nMoney: ${money_initially}")
    # Command to turn off the coffee machine
    elif guess=="off":
        should_continue=False


    else:
        if MENU[guess]["ingredients"]["water"] > Water_initially:
            print("Sorry there is not enough water\n")
            continue
        if MENU[guess]["ingredients"]["coffee"] > Coffee_initially:
            print("Sorry there is not enough coffee\n")
            continue

        if guess!="espresso" and MENU[guess]["ingredients"]["milk"] > Milk_initially:
            print("Sorry there is not enough milk\n")
            continue

        # Use of continue is to ensure that no more than one ingredient's inadequate capacity is displayed
        else:
            print("Please insert coins.\n")
            quarters = int(input("How many quarters: "))
            dimes = int(input("How many dimes: "))
            nickles = int(input("How many nickles: "))
            pennies = int(input("How many pennies: "))
            print("\n")
            money_given_by_user = conversion_of_money(quarters, dimes, nickles, pennies)
            if money_given_by_user > MENU[guess]["cost"]:
                # We subtract the required capacity of ingredients needed for drink from the remaining ingredients in coffee machine
                change = change_given_back(money_given_by_user, guess, MENU)
                Water_initially -= MENU[guess]["ingredients"]["water"]
                Coffee_initially -= MENU[guess]["ingredients"]["coffee"]
                money_initially += MENU[guess]["cost"]
                # We do not need to check the availability of milk for espresso since it is not a required ingredient for its recipe
                if guess != "espresso":
                    Milk_initially -= MENU[guess]["ingredients"]["milk"]

                print(f"Here is ${round(change, 2)} in change.")
                print(f"Here is your {guess}. Enjoy!\n")
            elif money_given_by_user < MENU[guess]["cost"]:
                print("Sorry that's not enough money. Money refunded.\n")

