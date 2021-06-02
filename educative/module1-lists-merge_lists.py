def merge_lists(lst1, lst2):
    out = []

    i = j = 0

    while i < len(lst1):
        if lst1[i] < lst2[j]:
            out.append(lst1[i])
            i += 1
        else: 
            out.append(lst2[j])
            j += 1
    
    while j < len(lst2): 
        out.append(lst2[j])
        j += 1

    return out
    
    
# proper one line solution. 
def merge_lists_1line(lst1, lst2):
    return sorted(lst1 + lst2)



list1 = [1,3,4,5]  
list2 = [2,6,7,8]

print(merge_lists(list1, list2))
