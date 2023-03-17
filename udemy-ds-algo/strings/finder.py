def finder(arr1, arr2):
    arr2.sort()
    
    idx = 0
    for n in arr1: 
        if n != arr2[idx]:
            return n
        else: 
            idx += 1
            
def finder2(arr1, arr2):
    return list(set(arr1) ^ set(arr2))[0]            
            
ans1 = finder([1,2,3,4,5,6,7], [2,7,3,1,4,6])
ans2 = finder2([1,2,3,4,5,6,7], [2,7,3,1,4,6])

print(ans1)    
    