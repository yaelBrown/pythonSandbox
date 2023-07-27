# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        t = ""
        while head.next: 
            t = t + str(head.val)
            head = head.next
        t = t + str(head.val)

        return int(t, 2)