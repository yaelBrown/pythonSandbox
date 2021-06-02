def find_product(lst):
    idx = 0
    out = list()

    while idx < len(lst):
        prod = 1
        for n in lst: 
            if not lst.index(n) == idx:
                prod *= n
        out.append(prod)
        idx += 1

    return out


def find_product(lst):
    tot = 1
    for i in lst: 
        tot *= i

    return [tot/num for num in lst]