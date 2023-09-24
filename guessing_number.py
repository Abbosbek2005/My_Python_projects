from random import randint
"""
This 
"""

easy_level_turns = 10
hard_level_turns = 5 

# Function to check user's guess against actual answer
""" Checks answer against guess. Returns the number of turns remaining"""
def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

# Make function to set difficulty

def set_difficulty():
    level=input("Choose difficulty. Type easy or hard: ")
    if level == "easy":
        return easy_level_turns
    else:
        return hard_level_turns

def game():

# Choose random number between 1 to 100 


    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer=randint(1,100)

    turns = set_difficulty()
    print(f"You have {turns} attempts remaining  to guess the number. ")

# Repeat the guessing functionality if they get it wrong.

    guess = 0
    while guess != answer:

        # Let the user guess a number

        guess = int(input("Make a guess: "))

        check_answer(guess, answer,turns)
        if turns == 0:
            print("You have run out of guesses, you lose!")
        elif guess != answer:
            print("Guess again")
game()
    



    



                