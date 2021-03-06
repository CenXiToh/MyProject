#!/usr/bin/env python
# coding: utf-8

# In[1]:


from IPython.display import clear_output


# In[2]:


def display_board(board):
    clear_output()
    
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])


# In[3]:


def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
        
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O','X')


# In[4]:


def place_marker(board,marker,position):
    board[position] = marker


# In[5]:


def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # horizontal top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # horizontal middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # horizontal bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # vertical left
    (board[8] == mark and board[5] == mark and board[2] == mark) or # vertical middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # vertical right 
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal


# In[6]:


import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# In[7]:


def space_check(board, position):
    return board[position] == ' '


# In[8]:


def full_board_check(board):
    for i in range (1,10):
        if space_check(board,i):
            return False
    return True


# In[9]:


def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position


# In[10]:


def replay():
    return input('Do you want to play again? (Yes or No)').lower().startswith('y')


# In[ ]:





# In[11]:


print('Welcome to Tic Tac Toe! ')
print('The number on each board represents the position you are going to choose')
print(' ' + '7' + ' | ' + '8' + ' | ' + '9')
print('----------')
print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
print('----------')
print(' ' + '1' + ' | ' + '2' + ' | ' + '3')


while True:
    theBoard = [' '] * 10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
        
    while game_on:
        
        if turn == 'Player 1':
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print('You won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('This game is a draw!')
                    break
                else:
                    turn = 'Player 2'
                    
                    
        else:
            # player 2's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)
            
            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('You won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('This game is a draw!')
                    break
                else:
                    turn = 'Player 1'
                    
    if not replay():
        break
                    


# In[ ]:




