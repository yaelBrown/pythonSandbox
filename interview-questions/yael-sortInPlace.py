import math

aa = [ 5, 4, 3, 2 ]

def reverseArr(arr): 
    pivot = math.ceil(len(aa) / 2)
    
    for i in range(0,len(arr)): 
        if i == pivot:
            break
        arr[i], arr[(len(arr) - 1) - i] = arr[(len(arr) - 1) - i], arr[i]
            
reverseArr(aa)            

print(aa)