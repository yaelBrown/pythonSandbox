def right_rotate(lst, k):
    if len(lst) == 0 or len(lst) == k: return lst
    idx = 0
    out = [None] * len(lst)

    # print({"lst": lst, "k": k})
    
    for n in lst: 
        out[(idx + k) % len(lst)] = n
        idx += 1
    
    return out

def right_rotate(lst, k):
    # get rotation index
    if len(lst) == 0:
        k = 0
    else:
        k = k % len(lst)
    return lst[-k:] + lst[:-k]


print(right_rotate([10, 20, 30, 40, 50], abs(3)))
