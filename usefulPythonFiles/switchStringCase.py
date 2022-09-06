import string

ltr = "A"
out = ""

def switchCase(s):
    out = ""
    for ltr in s: 
        if ltr in string.ascii_letters[:26]:
            out += ltr.upper()
        else:
            out += ltr.lower()
    
    return out
    
sentence = "This is A TEST sentence"
print(switchCase(sentence))

