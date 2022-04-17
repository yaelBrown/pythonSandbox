# import sys
# sys.setrecursionlimit(10000)

def fact(n, p = 1): 
    assert n >= 0 and int(n) == n, 'The number must be positive integer only'
    if n == 1 or n == 0: 
        return p
    else: 
        return n * fact(n-1, p)

print(fact(12))
print(fact(-12))
    
    
    
    
    
    
    