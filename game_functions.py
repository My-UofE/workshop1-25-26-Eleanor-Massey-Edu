import random

# function to be used by game_1: Guess the Number
def pick_value(poss_values):          #it seems like the test wants the pick_value function to always pick the middle of the possible values left
    middle_indices = [len(poss_values)//2]
    if len(poss_values) % 2 == 0:
        middle_indices.append((len(poss_values)//2)-1)
    random_index = random.choice(middle_indices)
    x = poss_values[random_index]   
    print(x)
    return x

pick_value([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

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
    '''letter is the letter that the user has just guessed, word is the word that has to be guessed,
    and board is a list of length of the number of letters the word has, and each element is '_'.
    Changed game_3 so that this function also updates the board because it seemed like it wouldn't
    work otherwise. Output a boolean for if the user guessed a correct letter, and output the board
    updated accordingly.
    '''
    found_letter = False
    for n in range (0,len(word)):
        if word[n] == letter:
            found_letter = True
            board[n] = letter
    return found_letter, board
    