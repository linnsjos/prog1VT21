#encoding=utf-8
import time
import random

''' Globala variabler '''

board = [' ',' ',' ',
         ' ',' ',' ',
         ' ',' ',' ']

player = "X"

game = True

winner = None


'''Funktionen är spelbrädet som skrivs ut.'''
def showboard():
    print(" ___ ___ ___") 
    print("|",board[0],"|",board[1],"|",board[2],"|","   1 | 2 | 3")    
    print("|___|___|___|")    
    print("|",board[3],"|",board[4],"|",board[5],"|","   4 | 5 | 6")  
    print("|___|___|___|")    
    print("|",board[6],"|",board[7],"|",board[8],"|","   7 | 8 | 9")   
    print("|___|___|___|")        
    
'''Denna funktion inskriver användarens input/datorns val till brädet.
   Output är brädet med den placering som inskrivits'''
def turn():
    if player == "X":
        global orientation
        orientation = intinput() - 1
        if board[orientation] == ' ':
            board[orientation] = player
        elif board[orientation] != ' ':
            orientation = occupiedcell() - 1
            board[orientation] = player
        showboard()        
    elif player == "O":
        print("Datorn väljer sin location...")
        time.sleep(2)
        computermove()
        showboard()

'''Funktionen tar ut de lediga platserna som datorn kan välja mellan.
   Returvärdet är en lista med de lediga platserna'''
def emptyspaces():
    emptyspace = []
    for i in range(len(board)):
        if board[i] ==' ':
            emptyspace.append((int)(str(i)))    
    return emptyspace

'''En funktion som sköter datorns val av placering med hjälp av andra funktioner. 
   Returvärdet är det val datorn valt'''
def computermove():
    while True:
        if cornermoves() == False:
            break
        elif middlemove() == False:
            break
        elif sidemoves() == False:
            break    
    
'''En funktion som undersöker om datorn först och främst kan välja hörn på brädet.
   Returvärdet är det hörn som datorn kunde välja om det var ledigt, annars returnerar
   den True vilket innebär att cornermoves inte ger något output i computermove().'''
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

'''En funktion som undersöker om datorn kan välja mitten om inget hörn är ledigt.
   Returvärdet är mitten som datorn kunde välja om det är ledigt, annars returnerar
   den True vilket innebär att middlemove inte ger något output i computermove().'''
def middlemove():
    thelist = emptyspaces()
    if 4 in thelist:
        board[4] = player
        return False
    else:
        return True

'''En funktion som undersöker om datorn kan välja sidoplaceringar om inget annat är tillgängligt.
   Returvärdet är den sidoplacering som datorn kunde välja om det var ledigt, annars returnerar
   den True vilket innebär att sidemoves inte ger något output i computermove().'''
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
    
'''Denna funktion undersöker användarens input på placering. Den undersöker först och främst om inputet är ett heltal.
   Sen undersöker den om inputet förhåller sig mellan 1 och 9. Returvärdet är ett korrekt input/placering.'''
def intinput():
    while True:
        if player == "X":
            orientation = input("Det är din tur att ange ett h\u0332e\u0332l\u0332t\u0332a\u0332l\u0332 mellan \u03321 och \u03329: ")
        elif player == "O":
            orientation = input("O - Ange ett h\u0332e\u0332l\u0332t\u0332a\u0332l\u0332 mellan \u03320 och \u03329: ")
        if (orientation.isdigit()):
            orientation = int(orientation)
            if orientation<=9:
                return orientation
        else:
            orientation = input("Ett h\u0332e\u0332l\u0332t\u0332a\u0332l\u0332 tack!: ")

'''Denna funktion ber om nytt användarinput om placeringen som valdes i intinput() var upptagen.
   Returvärdet är ett korrekt och ledigt input/placering'''
def occupiedcell():
    orientation = input("Tyvärr är platsen upptagen, välj en annan: ")
    while True:
        if (orientation.isdigit()):
            orientation = int(orientation)
            if orientation<=9:
                return orientation
        else:
            orientation = input("Ett h\u0332e\u0332l\u0332t\u0332a\u0332l\u0332 tack!: ")
            
'''Funktionen sköter byte av markering/spelare.
   Returvärdet är den nya markören.'''
def switchplayer():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return

'''Funktionen undersöker om spelet är över genom andra funktioner.'''
def gameover():
    win()
    tie()

'''Funktionen kontrollerar om det finns en vinnare genom andra funktioner.
   Returvärdet är den som vunnit om det finns en vinnare, eller inget om det inte finns någon vinnare.'''
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
            
'''I denna funktionen kollas det om det finns vinst på raderna.
   Returvärdet är False (spelet avbryts) och vilken markör som vunnit, eller inget.'''
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

'''I denna funktionen kollas det om det finns vinst på kolumnerna.
   Returvärdet är False (spelet avbryts) och vilken markör som vunnit, eller inget.'''
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

'''I denna funktionen kollas det om det finns vinst på diagonalerna.
   Returvärdet är False (spelet avbryts) och vilken markör som vunnit, eller inget.'''
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
 
'''Funktionen kollar om spelet är oavgjort.'''   
def tie():
    global game
    if ' ' not in board:
        game = False
        return True
    else:
        return False

'''Funktionen sköter användargränssnitt och introduktion av spelet'''
def playgame():
    print("Du valde att spela med AI.")
    time.sleep(1.5)
    print("Regler: \n Du börjar som X, datorn är O. \n Ni turas om att välja position på brädet. \n Man kan inte skriva över den andres position. \n Den som först får tre i rad vinner.")
    time.sleep(7)
    print("Detta är spelplanen:")
    showboard()
    time.sleep(2)
    while game:
        turn()
        gameover()
        switchplayer()
        emptyspaces()
    if winner == "X":
        print("Grattis du vann!")
    elif winner == "O":
        print("Du förlorade mot datorn!")
    elif tie:
        print("Det blev oavgjort. Ingen vinnare!")
    

'''inspiration/Pseudokod:
https://inventwithpython.com/chapter10.html
https://replit.com/@aaron_bernath/PythonTicTacToeApp'''
    
