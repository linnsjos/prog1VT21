#encoding=utf-8

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
    
def turn():
    global orientation
    '''count = 0'''
    orientation = intinput() - 1
    if board[orientation] == ' ':
        board[orientation] = player
       ''' count += 1'''
    elif board[orientation] != ' ':
        orientation = intinput2() - 1
        board[orientation] = player
        return player
    showboard()
    
    
def intinput():
    while True:
        orientation = input("Ange ett h\u0332e\u0332l\u0332t\u0332a\u0332l\u0332 mellan \u03321 och \u03329: ")
        if (orientation.isdigit()):
            orientation = int(orientation)
            if orientation>0 and orientation<=9:
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
        winner = diagonal_winner
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
      # Or return None if there was no winner
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
    diagonal1 = board[0] == board[4] == board[7] != ' '
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


'''def runningcode():
Vill du spela med AI eller din kompis?
Regler för den den väljer
Spela spelet
If winner or tie; vill du spela igen så börjas allt om

    print("Detta är din spelplan:")
    playgame()
    '''       
playgame()
