#encoding=utf-8 

'''Funktionen sorterar en lista. Förklaring på hur sorteringsalgoritmen fungerar och vad funktionen utför: shorturl.at/tGSW1.
Returvärdet är listan i sorterad ordning.
Parametrarna = listan (arr) är den lista som ska sorteras.'''
def insertionsort(arr):
        for i in range(len(arr)):
                for j in range(0,i):
                        if arr[i]<arr[j]:
                                temp = arr[i]
                                arr[i] = arr[j]
                                arr[j] = temp
        return arr


'''Funktionen innebär en testkod för att köra ovanstående funktioner till det syfte de ska användas till.
Även för att ovanstående kod ska köras med god användarvänlighet.
Parametrarna = listan (arr) är den lista som ska kontrolleras'''
def runtestcode(arr):
        print('-'*50)
        print("Din lista:", arr)
        sortedlist = insertionsort(arr)
        print("Din sorterade lista:", sortedlist)
 
runtestcode([5, 3, 2, 4, 1, 7, 9])
runtestcode([])
runtestcode([1,2,3])

#ordo = samma som på bubble sort = worst- och averagecase är O(N^2) medan bestcase är O(N).

