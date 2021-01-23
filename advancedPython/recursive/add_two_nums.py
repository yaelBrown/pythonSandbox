""" 
This works but not what leetcode wants
"""


# Definition for singly-linked list.
class Linked_List:
  def __init__(self, val):
    self.head = ListNode(val)
    self.size = 0

  def append(self, data):
    new_node = ListNode(data)       # create temp node based on supplied data
    cur = self.head

    while cur.next != None:     # find the last node in the LL
      cur = cur.next
    
    cur.next = new_node         # add new node to last node
    self.size =  self.size + 1

  def length(self):
    return self.size

  def get(self, idx):
    if idx > self.size:
      print("Index out of range")
      return None
    else: 
      cnt = idx
      cur = self.head
      while cnt != 0:
        cur = cur.next
        cnt -= 1
      return cur.val

  def __print__(self):
    cur = self.head

    while cur.next != None:
      cur.printNode()
      cur = cur.next
    cur.printNode()


class ListNode(object):
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
  
  def printNode(self):
    if 'val' in locals(): 
      nxt = self.next.val
    else: 
      nxt = None

    print({"value": self.val})

  def get(self):
    return self.val


class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    i = j = k = 0

    _ = ""
    __ = ""

    cnt = l1.length()
    
    while cnt > 1:
      _ += str(l1.get(cnt))
      cnt -= 1

    cnt = l2.length()
    
    while cnt > 1:
      __ += str(l2.get(cnt))
      cnt -= 1

    sum = int(_) + int(__)

    print(_ + " + " + __ + " = " + str(sum))

    out = Linked_List(int(str(sum)[0]))
    cnt = 0

    while cnt < len(str(sum)):
      out.append(str(sum)[cnt])
      cnt += 1

    out.__print__()

    return out




if __name__ == "__main__":
  aa = Linked_List(1)
  aa.append(2)
  aa.append(3)
  aa.append(4)

  aa.length()

  aa.__print__()

  # print({"2": aa.get()})

  l1 = [9,9,9,9,9,9,9]
  l2 = [9,9,9,9]

  _ = l1
  __ = l2

  l1 = Linked_List(l1[0])
  for i in _:
    if i == 0:
      i += 1
      continue
    l1.append(i)

  l2 = Linked_List(l2[0])
  for k in __:
    if i == 0:
      i += 1
      continue
    l2.append(k)

  Solution.addTwoNumbers(None, l1,l2)