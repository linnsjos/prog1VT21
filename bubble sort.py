#encoding=utf-8 

'''Funktionen sorterar en lista. Funktionen jämför två index (ex. (0 och 1) med dess element, om det första elementet är större än det
andra elementet så byter dem plats och ett nytt element (index 2) jämförs mot det tidigare största elementet,
detta sker genom hela listan tills alla element har jämförts och hittat sin plats.
Returvärdet är listan i sorterad ordning.
Parametrarna = listan (arr) är den lista som ska sorteras.'''
def bubblesort(arr):
    for i in range(1,len(arr)): # - 1?
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]: 
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

'''Funktionen innebär en testkod för att köra ovanstående funktioner till det syfte de ska användas till.
Även för att ovanstående kod ska köras med god användarvänlighet. 
Parametrarna = listan (arr) är den lista som ska kontrolleras'''
def runtestcode(arr):
    print('-'*50)
    print("Din lista:", arr)
    sortedlist = bubblesort(arr)
    print("Din sorterade lista:", sortedlist)
 
runtestcode([5, 3, 2, 4, 1, 7, 9])
runtestcode([])
runtestcode([1,2,3])

#ordo = worst- och averagecase är O(N^2) medan bestcase är O(N).
