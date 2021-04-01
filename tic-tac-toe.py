#encoding=utf-8

board = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']

player = "O"

game = True


def showboard():
    print(" ___ ___ ___") 
    print("|",board[0],"|",board[1],"|",board[2],"|")    
    print("|___|___|___|")    
    print("|",board[3],"|",board[4],"|",board[5],"|")  
    print("|___|___|___|")    
    print("|",board[6],"|",board[7],"|",board[8],"|")   
    print("|___|___|___|")        
        

def playgame():
    while game:
        turn()
    
def turn():
    '''for i in range(0,9):
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
    

def switchplayer():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return
        
        
def winner():
    checkrow()
    checkcolumn()
    checkdiagonal()

def checkrow(): '''FÅ DETTA ATT FUNGERA?'''
    row1 = board[0] == board[1] == board[2] != ""
    row2 = board[3] == board[4] == board[5] != ""
    row3 = board[6] == board[7] == board[8] != ""
    
    if row_1 or row_2 or row_3:
        global game
        game = False
    if row_1:
        return board[0] 
    elif row_2:
        return board[3] 
    elif row_3:
        return board[6] 
      # Or return None if there was no winner
    else:
        return None    
    
def checkcolumn():
    return
    
def checkdiagonal():
    return
        
#def checkwins = rows, column and diagonal.


def runningcode():
    playgame()
    winner()

runningcode()