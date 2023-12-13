# Blackjack game:
# The deck is unlimited in size.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
# The cards in the list have equal probability of being drawn
import random
def deal_card():
    # gets the cards (shuffle it)
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random.choice(cards)
    return cards

def calculate_score(cards):
     """ Take a list of cards and return the score calculated from the cards"""
     if sum(cards) == 21 and len(cards) == 2:
           return 0
     if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
     return sum(cards)
def compare(user_score, computer_score):
     if user_score==computer_score:
          return "DRAW"
     elif computer_score==0:
          return "LOSE, opponent has blackjack"
     elif user_score>21:
          return "You went over, you lose"
     elif computer_score>21:
          return "Opponent went over, you win"
     elif user_score>computer_score:
          return "You win"
     else:
          return "You lose"
def play_game():
     user_cards = []
     computer_cards = []
     is_game_over = False

     for _ in range(2):
          new_cards = deal_card()
          user_cards.append(new_cards) 
          computer_cards.append(deal_card)

     while not is_game_over:
          user_score = calculate_score(user_cards)
          computer_score = calculate_score(computer_cards)
          print(f" Your cards: {user_cards}, currentscore: {user_score}")
          print(f" Computer's first card: {computer_cards[0]}")
          if user_score == 0 or computer_score == 0 or user_score > 21:
               is_game_over = True
          else:
               user_should_deal=input("Type 'y' to get another card, type 'n' to pass: ")
               if user_should_deal=='y':
                    user_cards.append(deal_card())
               else:
                    is_game_over=True
     while computer_score!=0 and computer_score<17:
          computer_cards.append(deal_card())
          computer_score=calculate_score(computer_cards)
     print(f"your final hand: {user_cards}, final score: {user_score}")
     print(f"computer's final hand: {computer_cards}, final score: {computer_score}")
     print(compare(user_score,computer_score))
    


          
          
               
          


     
