from Stack import MyStack

def next_greater_element(lst):
    if len(lst) == 0: return -1

    j = 0
    k = 1

    out = []

    while j < len(lst):
      temp = lst[j]

      for l in lst:
        if k < len(lst):
          if l > lst[k]:
            out.append(lst[k])
            break
          else: 
            k += 1
            continue
        else:
          out.append(-1)

      j += 1




def next_greater_element(lst):
  if len(lst) == 0: return -1
    
  j = 0
  k = 1
    
  out = []
    
  while j < len(lst):
    temp = lst[j]
    
    for l in lst:
      if l is lst[j]: 
        continue
        
      if k < len(lst):
        if l > lst[j]:
          out.append(lst[k])
          break
        else: 
          k += 1
          continue
      else:
        out.append(-1)
    
    j += 1
      
  return out




test = [4, 6, 3, 2, 8, 1]

print(next_greater_element(test))





def next_greater_element(lst):
    stack = MyStack()
    res = [-1] * len(lst)
    for i in range(len(lst) - 1, -1, -1):
        if not stack.is_empty():
            while not stack.is_empty() and stack.peek() <= lst[i]:
                stack.pop()
        if not stack.is_empty():
            res[i] = stack.peek()
        stack.push(lst[i])
    return res


