# Blackjack Game Project

#---------------------

# Modules imported
import random
import art

# Blackjack game loop
def Blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = [] # User's card picks are stored here
    dealer_cards = [] # Dealer's card picks are stored here
    for random_value in range(0, 2):
        user_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
    sum_of_user = 0
    sum_of_dealer = 0
    for card in user_cards:
        sum_of_user += card
    for card in dealer_cards:
        sum_of_dealer += card
    should_continue = True

    # Conditional statement for when both user and dealer hit blackjack in the first two card draws
    if sum_of_dealer == 21 and sum_of_user == 21:
        if len(user_cards) == 2 and len(dealer_cards) == 2:
            print(f"Your final hand: {user_cards}, final score is {sum_of_user}")
            print(f"Dealers's final hand: {dealer_cards}, final score is {sum_of_dealer}")
            print("You both got blackjack!")
            should_continue = False
    # Conditional statement for when only user hits blackjack in first two cards
    elif sum_of_user == 21:
        if len(user_cards) == 2:
            print(f"Your final hand: {user_cards}, final score is {sum_of_user}")
            print(f"Dealers's final hand: {dealer_cards}, final score is {sum_of_dealer}")
            print("You got blackjack!")
            print("You win!")
            should_continue = False
    # Conditional statement for when only dealer hits blackjack in first two cards
    elif sum_of_dealer == 21:
        if len(dealer_cards) == 2:
            print(f"Your final hand: {user_cards}, final score is {sum_of_user}")
            print(f"Dealers's final hand: {dealer_cards}, final score is {sum_of_dealer}")
            print("Dealer got blackjack!")
            print("You lose!")
            should_continue = False

    while should_continue:
        print(f"Your cards: {user_cards}, current score is {sum_of_user}")
        print(f"Dealer's first card is {dealer_cards[0]}")

        ask_for_card = input("Do you want to take another card(yes/no): ").lower()

        # User chooses to draw another card.
        if ask_for_card == "yes":
            user_cards.append(random.choice(cards))
            sum_of_user += user_cards[-1]


            if sum_of_user > 21:
                # Convert Ace from 11 to 1 if sum of all user cards is more than 21
                while sum_of_user > 21 and 11 in user_cards:
                    user_cards[user_cards.index(11)] = 1
                    sum_of_user -= 10
                # User loses if sum of all cards is over 21 despite removing all 11s
                if sum_of_user > 21:
                    print(f"Your cards: {user_cards}, current score is {sum_of_user}")
                    print(f"Dealer's first card is {dealer_cards[0]}")
                    print("You lose!")
                    print("You went over 21!")
                    should_continue = False
                else:
                    should_continue = True

        # User does not draw a new card
        elif ask_for_card=="no":
            # Dealer must draw until sum of cards is more than 17
            while sum_of_dealer < 17:
                dealer_cards.append(random.choice(cards))
                sum_of_dealer += dealer_cards[-1]
            # Convert Ace from 11 to 1 if sum of all user cards is more than 21
            while sum_of_dealer > 21 and 11 in dealer_cards:
                dealer_cards[dealer_cards.index(11)] = 1
                sum_of_dealer -= 10

            print(f"Your final hand: {user_cards}, final score is {sum_of_user}")
            print(f"Dealers's final hand: {dealer_cards}, final score is {sum_of_dealer}")
            if sum_of_user > 21:
                print("You went over 21!")
                print("You lose!")
                should_continue = False
            elif sum_of_dealer > 21:
                print("The dealer went over 21")
                print("You win!")
                should_continue = False

            # Comparing sum of user and dealer cards to determine winner
            elif sum_of_user > sum_of_dealer:
                print("You win!")
                should_continue = False
            elif sum_of_dealer > sum_of_user:
                print("You lose!")
                should_continue = False

# User input to get game started
start_game=input("Do you want to play a game of Blackjack(yes/no)?\n").lower()
while start_game=="yes":
    print(art.logo)
    Blackjack()
    start_game = input("Do you want to play a game of Blackjack(yes/no)?\n").lower()
    if start_game=="yes":
        print("\n" * 100)

