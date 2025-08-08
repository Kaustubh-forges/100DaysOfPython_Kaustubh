# Higher or Lower Game Project

#------------------------------

import random
import game_data
import art
# Generates a random number that will be used to randomize selection from "data" list
def Random_data_picked():
    random_pick = random.randint(0, len(game_data.data) - 1)
    # Randomly pick a celebrity/organization with their name,description,country,and follower count + Accesses the dictionaries in list "data"
    random_entity_name=game_data.data[random_pick]['name']
    random_entity_description=game_data.data[random_pick]['description']
    random_entity_country=game_data.data[random_pick]['country']
    random_entity_follower_count=game_data.data[random_pick]['follower_count']

    return [random_entity_name,random_entity_description,random_entity_country,random_entity_follower_count]

def comparison(count1,count2,score):
    user_choice=input("Who has more followers? Type 'A' or 'B': ")
    if count1>count2:
        if user_choice=="A":
            score+=1
            print("\n")
            print(f"You are right! Current score is {score}\n")
            return score
        elif user_choice=="B":
            score=0
            print("\n"*20)
            print(f"Sorry that's wrong! Final score is now {score}")
            return score

    elif count1<count2:
        if user_choice=="A":
            score=0
            print("\n"*20)
            print(f"Sorry that's wrong! Final score is now {score}")
            return score
        elif user_choice=="B":
            score += 1
            print("\n")
            print(f"You are right! Current score is {score}\n")
            return score

def game():
    should_continue=True
    result=0
    score=0
    while should_continue:
        if result!=0:
            # Randomly picks a new celebrity if both competitors are the same
            if person_b==person_a:
                person_b=Random_data_picked()

            # Shifts competitor B to competitor A's position and generate a new competitor to compare with
            person_a=person_b
            count1=person_b[3] # Accesses the follower count returned by the list from the "Random_data_picked()" function
            person_b=Random_data_picked()
            count2=person_b[3] # Accesses the follower count returned by the list from the "Random_data_picked()" function
        else:
            # Random instagram accounts are assigned in the form of lists
            person_a = Random_data_picked()
            person_b = Random_data_picked()
            # Randomly picks a new celebrity if both competitors are the same
            if person_b==person_a:
                person_b=Random_data_picked()
            count1 = person_a[3]  # Accesses the follower count returned by the list from the "Random_data_picked()" function
            count2 = person_b[3]  # Accesses the follower count returned by the list from the "Random_data_picked()" function

        print(f"Compare A: {person_a[0]}, a {person_a[1]}, {person_a[2]}")
        print(art.vs)
        print(f"Against B: {person_b[0]}, a {person_b[1]}, {person_b[2]}")

        score=result # User score after every comparison round
        result=comparison(count1,count2,score)
        # Game discontinued after user loses( user's score is automatically reset to 0 after loss)
        if result==0:
            should_continue=False

start=input("Do you want to play Higher or Lower? Type 'yes' or 'no': ")
if start=="Yes" or start=="yes":
    print(art.logo)
    game()
else:
    print("Oh...I guess you have better things to do then😒")