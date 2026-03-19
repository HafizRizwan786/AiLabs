"""
import random,string

def initial_state():
    return random.randint(5,10)

def possible_new_states(state):
    return [state-take for take in (1,2,3) if take<=state]

def evaluate(state,is_maximizing):
    if state==0:
        return +1 if is_maximizing else -1
    return None

def minimax(state,is_maximizing):
    score=evaluate(state,is_maximizing)
    if score is not None:
        return score
    
    moves=[
        minimax(new_state,not is_maximizing)
        for new_state in possible_new_states(state)
    ]
    
    return max(moves) if is_maximizing else min(moves)
    

def best_move(state):
    return max (
        possible_new_states(state),
        key=lambda s:minimax(s,is_maximizing=True)
    )

def game_over(score):
    print("You win!" if score > 0 else "I win!")

def input_choice(choices,text="Choose: "):
    inputs=dict(zip(string.ascii_letters,choices))
    for letter, choice in inputs.items():
        print(f"{letter} {choice}")
    while True:
        c=input(text)
        if c in inputs:
            return inputs[c]
        print(f'Select one of {','.join(inputs)}')

def Nim_Game():
    state=initial_state()
    while True:
        print(f'Current State: {state}')
        state=input_choice(possible_new_states(state))
        score=evaluate(state,is_maximizing=False)
        if score is not None:
            return game_over(score)
        
        ai_move=best_move(state)
        print(f'I move from {state} to {ai_move}')
        state=ai_move
        score=evaluate(state,is_maximizing=True)
        if score is not None:
            return game_over(score)
        

Nim_Game()
"""


import math
board=[" " for _ in range(0,9)]

def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print('--+---+--')
    print(board[3] + " | " + board[4] + " | " + board[5])
    print('--+---+--')
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):
    win_condition=[
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    
    for condition in win_condition:
        if board[condition[0]]==board[condition[1]]==board[condition[2]]==player:
            return True
    return False

def board_full():
    return " " not in board


def minimax(is_maximizing):
    if check_winner('X'):
        return -1
    
    if check_winner('O'):
        return 1
    
    if board_full():
        return 0
    
    if is_maximizing:
        best_score= -math.inf
        for i in range(9):
            if board[i]==' ':
                board[i]='O'
                score=minimax(False)
                board[i]=' '
                best_score=max(best_score,score)
        return best_score
    else:
        best_score= math.inf
        for i in range(9):
            if board[i]==' ':
                board[i]='X'
                score=minimax(True)
                board[i]=' '
                best_score=min(best_score,score)
        return best_score


def best_move():
    best_score= -math.inf
    move=None
    
    for i in range(9):
        if board[i]==' ':
            board[i]='O'
            score=minimax(False)
            board[i]=' '
            if score>best_score:
                best_score=score
                move=i
            
    return move


def player_move():
    while True:
        move=int(input('Enter a position (1-9): '))-1
        if board[move]==" ":
            board[move]='X'
            break
        else:
            print('Invalid position!!!')


def ai_move():
    move=best_move()
    board[move]='O'
    print(f'Ai choose position {move+1}')



def Tic_Toc_Game():
    print("Positions are: ")
    print("1 | 2 | 3")
    print('--+---+--')
    print("4 | 5 | 6")
    print('--+---+--')
    print("7 | 8 | 9")
    
    while True:
        print_board()
        player_move()
        if check_winner('X'):
            print_board()
            print('Congratulations! you have won the game.')
            break
        
        if board_full():
            print_board()
            print('Game have been drawn!')
            break
        
        ai_move()
        if check_winner('O'):
            print_board()
            print('Ai have won the game.')
            break
        
        if board_full():
            print_board()
            print('Game have been drawn!')
            break

Tic_Toc_Game()