aa = [1,2,3,4,6,5]

def arr_in_order(arr):
    i = 0
    j = 1
    
    while j <= (len(arr) - 1):
        if arr[i] > arr[j]:
            return "Not in order"
        else:
            i += 1
            j += 1
    
    return "In order :)"
    
    
print(arr_in_order(aa))
        