def find_sum(lst, k):
    for i in lst: 
        chk = k - i
        if chk in lst:
            return [i, chk]

    return []
