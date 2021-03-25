#encoding=utf-8
import random

'''Datorn gissar på användarens uttänkta tal i ett visst intervall. Detta med hjälp av binärsökning och vad användaren lägger in för input.
Returvärdet är användarens valda tal. '''

def computer_guessing_number():
    range_start= n_the_range[0]
    range_end= n_the_range[len(n_the_range)-1]
    print("Svara ja om talet är rätt. Om talet inte är rätt tala om för datorn ifall talet är större eller mindre.")
    while True:
        middle = (range_start + range_end) // 2
        guess = input("Är ditt tal " + str(middle) + "?: ")
        if "nej" and "större" in guess:
            range_start = middle
        elif "nej" and "mindre" in guess:
            range_end = middle
        elif "nej" in guess:
            middle = middle
            print("Tala om för datorn om talet är större eller mindre. Eventuellt kontrollera din stavning.")
        elif "ja" or "rätt" in guess:
            return middle


'''Funktionen innebär en testkod för att köra ovanstående funktioner till det syfte de ska användas till.
Även för att ovanstående kod ska köras med god användarvänlighet. '''

def runtestcode():
    print("Ditt sökintervall: ",the_range)
    print("Tänk ut ett tal datorn ska gissa fram!")
    number = computer_guessing_number()
    print("Datorn gissade sig fram till att ditt tal är", number)

#intervallet som talet gissas inom (i en lista):
the_range = input('Ange ett sökintervall för talet (Ex."1-100"): ')
n_the_range= the_range.split("-")
n_the_range = list(map(int, n_the_range))
listrange= list(range(n_the_range[0],n_the_range[1]+1))    

runtestcode()

