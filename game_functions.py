import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):
    x = random.choice(poss_values)   
    return x

# function to be used in game_2: Higher or Lower
def check_higher_lower(current_val, next_val, user_input):
    '''takes the last 2 values in the sequence, and outputs a boolean depending on if the user has correctly
    predicted that the last value is higher or lower than the penultemate value'''
    if current_val > next_val:
        answer = 'l'
    else:
        answer = 'h'
    if user_input == answer:
        return True
    else:
        return False

# function to be used in game_3: Hangman
def process_guess(letter, board, word):
    pass