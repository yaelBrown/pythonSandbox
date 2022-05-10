# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1.next is None and l2.next is None: 
            return ListNode((l1.val+l2.val))
        
        temp = ""
        temp2 = ""
        
        cur = l1 
                
        while cur.next:
            temp += str(cur.val)
            cur = cur.next
        temp += str(cur.val)
        
        cur = l2
        
        while cur.next: 
            temp2 += str(cur.val)
            cur = cur.next
        temp2 += str(cur.val)
        
        sum = str(int(temp) + int(temp2))[::-1]
        
        prev = None
        
        temp = []        

        for i in range(len(sum)): 
            temp.append(ListNode(int(sum[i])))
            
        for j in range(len(temp)):
            if (j+1) < len(temp):
                temp[j].next = temp[j+1]
        
        out = temp[0]
        
        return out
        
        