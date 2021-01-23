#1
def reverseString(s):
  print(s[::-1])

#2
def revrevString(t):
  out = rshelper(t, "")
  print(out)

def rshelper(s, slate):
  if len(s) == 1:
    print(slate + s)
  else:
    slate += s[-1]
    rshelper(s[:-1], slate)

#3
def reverseString(s): #16ms
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    i = 0
    j = len(s) - 1
    _ = ""
    __ = ""
    
    while i < 0:
        _ = s[i]
        __ = s[j]
        s[i] = s[j]
        s[j] = s[i]
        i += 1
        j -= 1

#4
def reverseString(s):
    """
    :type s: List[str]
    :rtype: None Do not return anything, modify s in-place instead.
    """
    i = 0
    j = len(s) - 1
    _ = ""
    
    while j > 0:
        _ = s[i]
        s[i] = s[j]
        s[j] = _
        i += 1
        j -= 1

#5
def reverseString(s):
  s.reverse()


if __name__ == "__main__":

  string = "cookies"

  reverseString(string)

  rshelper(string, "")