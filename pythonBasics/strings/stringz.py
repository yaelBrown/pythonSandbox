# https://medium.com/javarevisited/top-21-string-programming-interview-questions-for-beginners-and-experienced-developers-56037048de45


aa = "cookies"

def reverse(s):
    return s[::-1]

def duplicates(s):
    t = []
    
    for c in s: 
        if c in t: 
            print(c)
        else: 
            t.append(c)

    return 

bb = "popcorn"
bbb = "poxop"

def anagram(w1, w2):
    
    out = True
    for c in w1:
        if c in w2: 
            continue
        else: 
            return False
    return out
















print(anagram(bbb, bb))


# print(duplicates(aa))

