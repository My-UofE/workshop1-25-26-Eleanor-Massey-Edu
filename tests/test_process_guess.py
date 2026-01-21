from game_functions import process_guess

def test_process_guess():
    word = "banana"
    
    board = ['_','_','_','_','_','_']
    result, board = process_guess('b',board, word)         #need to change the board in the process_guess function so have to store that in a variable as well
    assert result == True
    assert board == ['b','_','_','_','_','_']


    board == ['b','_','_','_','_','_']
    result, board = process_guess('a',board, word)
    assert result == True
    assert board == ['b','a','_','a','_','a']

    board == ['b','a','_','a','_','a']
    result, board = process_guess('c',board, word)
    assert result == False
    assert board == ['b','a','_','a','_','a']