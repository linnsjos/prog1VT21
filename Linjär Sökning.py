# encoding=utf-8

'''Funktionen eftersöker ett angivet tal i en osorterad lista. Funktionen går igenom alla element på listan och jämför indexena med det talet som eftersöks.
Returvärdet är indexet på det angivna talet i listan. Om index<0 => talet finns inte i listan.
Parametrarna = listan (numbers) som det angivna talet (n) ska jämföras mot och eftersökas i.'''

def find(numbers,n):
    position= -1
    for i in numbers:
        if i == n:
            return position + 1
        else:
            position+=1
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
    print("Din lista:",numbers)
    n = intinput()
    print("Det eftersökta talet:",n)
    position = find(numbers,n)
    if (position >= 0):
        print(n, "finns på plats", position+1)
    else:
        print(n, "finns inte med i listan")
        
#den angivna listan som n tittas mot:
numbers = [5, 3, 2, 4, 1, 7, 9]

runtestcode()
runtestcode()
runtestcode()

'''Hur många jämförelser krävs för linjär sökning för en lista med 1000 element?: Worst case. Det krävs 1000 jämförelser, eftersom den går igenom alla element och worst case = ett tal
som ej finns i listan eller som är det sista talet i listan = den måste gå igenom hela listan = 1000 element = 1000 jämförelser.'''



