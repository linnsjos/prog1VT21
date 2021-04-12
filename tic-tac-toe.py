#encoding=utf-8

board = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']

player = "O"

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
    showboard()
    while game:
        turn()
        gameover()
        switchplayer()
    
def turn():
    count = 0
    showboard()
    orientation = int(input("Välj en plats mellan 1-9: ")) #check for smaller or bigger than 1 and 9
    orientation = orientation - 1
    if board[orientation] == ' ':
        board[orientation] = player
        count += 1
    else:
        while board[orientation] != ' ':
            orientation = int(input("Tyvärr är platsen upptagen, välj en annan: "))
            orientation = orientation - 1
            board[orientation] = player
    

def switchplayer():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return

def gameover():
    winner()
    tie()
        
        
def winner():
    global winner
    rowwinner = checkrow()
    columnwinner = checkcolumn()
    diagonalwinner = checkdiagonal()
    # Get the winner
    if rowwinner:
        winner = rowwinner
    elif columnwinner:
        winner = columnwinner
    elif diagonalwinner:
        winner = diagonal_winner
    else:
        winner = None    
            

def checkrow():
    row1 = board[0] == board[1] == board[2] != ""
    row2 = board[3] == board[4] == board[5] != ""
    row3 = board[6] == board[7] == board[8] != ""
    
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
    column1 = board[0] == board[3] == board[6] != ""
    column2 = board[1] == board[4] == board[7] != ""
    column3 = board[2] == board[5] == board[8] != ""
    
    if column1 or column2 or column3:
        global game
        game = False
    if column1:
        return board[0] 
    elif column2:
        return board[1] 
    elif column3:
        return board[2] 
      # Or return None if there was no winner
    else:
        return None    
    
def checkdiagonal():
    diagonal1 = board[0] == board[5] == board[8] != ""
    diagonal2 = board[2] == board[5] == board[7] != ""
    
    if diagonal1 or diagonal2:
        global game
        game = False
    if diagonal1:
        return board[0] 
    elif diagonal2:
        return board[2] 
      # Or return None if there was no winner
    else:
        return None     
        
#def checkwins = rows, column and diagonal.

def tie():
    # Set global variables
    global game
    # If board is full
    if "-" not in board:
        game = False
        return True
    # Else there is no tie
    else:
        return False


def runningcode():
    print("Detta är din spelplan:")
    playgame()
        

runningcode()

''' Skit
for i in range(0,9):
            switchplayer()
            count = 0
            showboard()
            orientation = int(input("Välj en plats mellan 1-9: ")) #check for smaller or bigger than 1 and 9
            orientation = orientation - 1
            if board[orientation] == ' ':
                board[orientation] = player
                count += 1
            else:
                while board[orientation] != ' ':
                    orientation = int(input("Tyvärr är platsen upptagen, välj en annan: "))
                orientation = orientation - 1
                board[orientation] = player
    else:
        showboard()    '''