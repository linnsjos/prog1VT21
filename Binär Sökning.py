#encoding=utf-8
import random

'''Funktionen eftersöker ett angivet tal i en sorterad lista. Funktionen jämför värdet med medianen på viss intervall, är värdet större än medianen
blir det nya intervallet det mittersta talet till det största talet i listan, där samma procedur upprepas tills det angivna talet är hittat.
Returvärdet är indexet på det angivna talet i listan. Om index<0 => talet finns inte i listan.
Parametrarna = listan (snumbers) som det angivna talet (n) ska jämföras mot och eftersökas i.'''

def binarysearch(snumbers,n):
    range_start = 0
    range_end = len(snumbers)-1
    middle = ""

    while range_start<= range_end:  
        middle = (range_start + range_end) // 2 
        if snumbers[middle] < n: 
            range_start = middle + 1
        elif snumbers[middle] > n:
            range_end = middle - 1
        else:
            return middle
    return -1


'''Funktionen finns för ett användargränssnitt som tillåter användaren göra vanliga användarfel, detta när använderen ger input och värdet ej är korrekt angivet. 
Funktionen korrigerar i detta fall mellanslag och omvandlar input till integer. Inte förens detta är kontrollerat returneras ett värde'''

def intinput():
    while True:
        number = input("Vilket tal vill du eftersöka?: ")
        n = number.replace(" ", "")
        if (n.isdigit()):
            n = int(n)
            return n
        else:
            print("Vänligen ange ett h\u0332e\u0332l\u0332t\u0332a\u0332l\u0332 i siffror!")

'''Funktionen innebär en testkod för att köra ovanstående funktioner till det syfte de ska användas till.
Även för att ovanstående kod ska köras med god användarvänlighet. '''

def runtestcode():
    print("-"*50)
    print("Din lista:",snumbers)
    n = intinput()
    print("Ditt eftersökta tal är:",n)
    position = binarysearch(snumbers,n)
    if (position >= 0):
        print(n,"finns på plats",position+1)
    else:
        print(n,"finns tyvärr inte med i listan")

#den sorterade listan:
numbers = list(range(1,101))
ranlist = random.sample(numbers, k=20)
snumbers = sorted(ranlist)

runtestcode()
runtestcode()
runtestcode()

'''Hur många jämförelser krävs för linjär sökning för en lista med 1000 element?: Worst case. Det krävs 10 jämförelser. (Har läst att worst case complexity
är O(log n) men jag testade och kom fram till 10 jämförelser innan det sista/första talet i listan hittades eller tills funktionen "ger upp".'''