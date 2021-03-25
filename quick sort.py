#encoding=utf-8

''' Pseudokod: https://www.researchgate.net/figure/Pseudocode-of-quicksort-adapted-from-1_fig1_332434596 '''
'''Funktionen sorterar en lista. Funktionen tar ut ett pivot och jämför resterande tal i listan mot det, beroende på om talet
är mindre, större, eller lika stort så sorteras dom in i olika listor som sedan sorteras/jämförs på samma sätt för att sedan 
sättas ihop till en hel sorterad lista. 
Returvärdet är listan i sorterad ordning.
Parametrarna = listan (arr) är den lista som ska sorteras.'''
def quicksort(arr):    
    if len(arr) < 1:
        return arr
    else:
        pivot = arr.pop()
    
    smallernumbers = []
    largernumbers = [] 
    equalnumbers = []    
    for i in arr:
        if i > pivot:
            largernumbers.append(i)
        elif i < pivot:
            smallernumbers.append(i)
        else:
            equalnumbers.append(i)
            
    return quicksort(smallernumbers) + quicksort(equalnumbers) + [pivot] + quicksort(largernumbers)


'''Funktionen finns för att kontrollera om användarens input är integer
Parametrarna = nummer (numbers) är de tal som ska kontrolleras'''
def intcheck(numbers):
    res = False
    numbers = numbers.replace(" ", "") #denna är nog inte mest effektiv och optimal men den fungerar
    if (numbers.isdigit()): #lösningen stödjer ej minustal
        res = True  
    return res

'''Funktionen finns för ett användargränssnitt som tillåter användaren göra vanliga användarfel, detta när använderen ger input och värdet ej är korrekt angivet. 
Funktionen korrigerar i detta fall mellanslag och omvandlar input till integer. Inte förens detta är kontrollerat returneras listan och
kan användas till sorteringsalgoritmen'''
def array():
    inputok = False
    while not inputok:
        numbers = input('Ange de positiva heltal du vill sortera med ett mellanrum ex: 1 2 3 4: ')
        inputok = intcheck(numbers)
        if not inputok:
            print("Bara p\u0332o\u0332s\u0332i\u0332t\u0332i\u0332v\u0332a\u0332 h\u0332e\u0332l\u0332t\u0332a\u0332l\u0332 tack!")
        
    arr = numbers.split()
    for i in range(len(arr)): 
        arr[i] = int(arr[i]) 
        
    return arr      

'''Funktionen innebär en testkod för att köra ovanstående funktioner till det syfte de ska användas till.
Även för att ovanstående kod ska köras med god användarvänlighet.
Parametrarna = listan (arr) är den lista som ska kontrolleras'''
def runtestcode(arr):
    print('-'*50)
    if arr == "":
        arr = array()
        print("Din lista:", arr)
    else:
        print("Din lista:", arr)
    sortedlist = quicksort(arr)
    print("Din sorterade lista:", sortedlist)

runtestcode("")
runtestcode([5, 3, 2, 4, 1, 7, 9])
runtestcode([])
runtestcode([1,2,3])

'''ordo - best- och averagecase är O(N log N) medan worstcase är O(N^2), jag har kodat efter worstcase
eftersom .pop() automatiskt tar det sista värdet.
Man räknar på att quick sort är effektivare i och med att inga tal behöver byta plats och att man har ett pivot som styr
sorteringen, vilket gör att algoritmen generellt sätt är bättre i prestanda i jämförelse mot bubble sort.'''