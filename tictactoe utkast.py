#encoding=utf-8

import os
import time

'''Inspo:
https://inventwithpython.com/chapter10.html
https://replit.com/@aaron_bernath/PythonTicTacToeApp'''

import random

board = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']

player = "X"

game = True

winner = None


def showboard():
    print(" ___ ___ ___") 
    print("|",board[0],"|",board[1],"|",board[2],"|")    
    print("|___|___|___|")    
    print("|",board[3],"|",board[4],"|",board[5],"|")  
    print("|___|___|___|")    
    print("|",board[6],"|",board[7],"|",board[8],"|")   
    print("|___|___|___|")        
        

def playgame():
    print("Detta är din spelplan")
    showboard()
    while game:
        turn()
        gameover()
        switchplayer()
        emptyspaces()
        cls()
        
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
def turn():
    if player == "X":
        global orientation
        orientation = intinput() - 1
        if board[orientation] == ' ':
            board[orientation] = player
        elif board[orientation] != ' ':
            orientation = intinput2() - 1
            board[orientation] = player
            return player
        showboard()        
    elif player == "O":
        print("Datorn väljer sin location")
        time.sleep(2)
        computermove()
        showboard()

def emptyspaces():
    emptyspace = []
    for i in range(len(board)):
        if board[i] ==' ':
            emptyspace.append((int)(str(i)))    
    return emptyspace
        
def computermove():
    while True:
        if cornermoves() == False:
            break
        elif middlemove() == False:
            break
        elif sidemoves() == False:
            break    
    
def cornermoves():
    thelist = emptyspaces()
    if 0 in thelist:
        board[0] = player
        return False
    elif 2 in thelist:
        board[2] = player
        return False
    elif 6 in thelist:
        board[6] = player
        return False
    elif 8 in thelist:
        board[8] = player
        return False
    else:
        return True

def middlemove():
    thelist = emptyspaces()
    if 4 in thelist:
        board[4] = player
        return False
    else:
        return True

def sidemoves():
    thelist = emptyspaces()
    if 1 in thelist:
        board[1] = player
        return False
    elif 3 in thelist:
        board[3] = player
        return False
    elif 5 in thelist:
        board[5] = player
        return False
    elif 7 in thelist:
        board[7] = player
        return False
    else:
        return True   
    
def intinput():
    while True:
        orientation = input("Ange ett h\u0332e\u0332l\u0332t\u0332a\u0332l\u0332 mellan \u03320 och \u03329: ")
        if (orientation.isdigit()):
            orientation = int(orientation)
            if orientation<=9:
                return orientation
        else:
            orientation = input("Ett h\u0332e\u0332l\u0332t\u0332a\u0332l\u0332 tack!: ")

def intinput2():
    while True:
        orientation = input("Tyvärr är platsen upptagen, välj en annan: ")
        if (orientation.isdigit()):
            orientation = int(orientation)
            if orientation<=9:
                return orientation
        else:
            orientation = input("Ett h\u0332e\u0332l\u0332t\u0332a\u0332l\u0332 tack!: ")
            

def switchplayer():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return

def gameover():
    win()
    tie()
        
        
def win():
    global winner
    rowwinner = checkrow()
    columnwinner = checkcolumn()
    diagonalwinner = checkdiagonal()
    if rowwinner:
        winner = rowwinner
    elif columnwinner:
        winner = columnwinner
    elif diagonalwinner:
        winner = diagonalwinner
    else:
        winner = None    
            

def checkrow():
    row1 = board[0] == board[1] == board[2] != ' '
    row2 = board[3] == board[4] == board[5] != ' '
    row3 = board[6] == board[7] == board[8] != ' '
    if row1 or row2 or row3:
        global game
        game = False
    if row1:
        return board[0] 
    elif row2:
        return board[3] 
    elif row3:
        return board[6] 
    else:
        return None    
    
def checkcolumn():
    column1 = board[0] == board[3] == board[6] != ' '
    column2 = board[1] == board[4] == board[7] != ' '
    column3 = board[2] == board[5] == board[8] != ' '
    if column1 or column2 or column3:
        global game
        game = False
    if column1:
        return board[0] 
    elif column2:
        return board[1] 
    elif column3:
        return board[2] 
    else:
        return None    
    
def checkdiagonal():
    diagonal1 = board[0] == board[4] == board[8] != ' '
    diagonal2 = board[2] == board[4] == board[6] != ' '
    if diagonal1 or diagonal2:
        global game
        game = False
    if diagonal1:
        return board[0] 
    elif diagonal2:
        return board[2] 
    else:
        return None     
        
def tie():
    global game
    if ' ' not in board:
        game = False
        return True
    else:
        return False
    
        
playgame()
