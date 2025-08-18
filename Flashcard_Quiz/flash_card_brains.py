# Class that manages and works the structure of the whole game
class flashcard_quiz:
    def __init__(self,list):
        # Initializes question number and score at the start of the game + Initializes the list that will be iterated
        self.question_number=0
        self.list=list
        self.score=0
    def still_has_cards(self):
        if self.question_number<len(self.list):
            return True
        else:
            return False
    def  move_to_next_question(self):
        current_question=self.list[self.question_number] # Gets one "flashcard" object per iteration. Self is not used as it is a simple variable
        self.question_number+=1
        guess=input(f"Q{self.question_number}. {current_question.definition}: ") # User is prompted to guess the answer
        self.check_answer(guess,current_question) # Self is used here as we implement another method of the "flashcard_quiz" class
    def  check_answer(self,guess,current_question):
        if guess.lower()==current_question.word.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("You got it wrong!")
        print(f"The right answer is {current_question.word}")
        print(f"Your score is {self.score}/{self.question_number}")