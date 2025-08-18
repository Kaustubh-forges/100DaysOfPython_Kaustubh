# Flashcard Quiz Game Project

#------------------------------

# Imported components from multiple files
from data import flashcard_data
from flashcard import flashcard
from flash_card_brains import flashcard_quiz

# Empty list will hold the whole quiz essentially
list_for_objects=[]

# Iterates through imported list that contains dictionaries of game data
for element in flashcard_data:
    word=element["word"]
    definition=element["definition"]
    object_for_each_flashcard=flashcard(word,definition) # Creates "flashcard" objects that contain a definition and word
    list_for_objects.append(object_for_each_flashcard) # Adds those objects to list so we can easily move through them one after another

object_for_quiz=flashcard_quiz(list_for_objects) # Creates an object that accesses the methods and attributes present in the class "flashcard_quiz"

# Accesses a method to check if whole list has been iterated + Meve to next object in list or end iteration if needed
while object_for_quiz.still_has_cards():
    object_for_quiz.move_to_next_question()

print("Congratulations! You have completed the quiz!")
print(f"Your final score is  {object_for_quiz.score}/{object_for_quiz.question_number}.")