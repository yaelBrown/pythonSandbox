"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

# this is not correct
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
  cur1 = l1
  cur2 = l2

  temp = None
  temp2 = []

  while cur1 != None or cur2 != None:
      temp = cur1.val + cur2.val
      if temp > 10:
          temp = temp - 10

      temp2.append(ListNode(temp))

      cur1 = cur1.next
      cur2 = cur2.next

  for i in range(len(temp2) - 1):
      temp2[i].next = temp2[i+1]

  return temp2[0]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        cur1 = l1
        cur2 = l2
        
        temp = ""
        temp2 = ""
        
        while cur1 != None or cur2 != None:
            temp += str(cur1.val)
            temp2 += str(cur2.val)
            
            cur1 = cur1.next
            cur2 = cur2.next
            

        
        outString = str(int(temp) + int(temp2))[::-1]
        
        cnt = 0
        nxt = None
        cur = None
        out = None
        for i in range(len(outString)):
            if cnt == 0: 
                cur = ListNode(int(outString[i]))
                out = cur
                cur.next = ListNode(int(outString[i+1]))
                cur = cur.next
                cnt += 1
                continue
            if i != (len(outString)-1):
                nxt = ListNode(int(outString[i+1]))
                cur.next = nxt
                print(cur)
                cnt += 1
                continue
            cnt += 1
        
            
        return out      