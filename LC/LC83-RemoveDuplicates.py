# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# o(n)
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        cur, prev = head, head

        seen = [cur.val]
        idx = 0

        #? 
        while cur != None:
            if idx != 0:
                if cur.val in seen:
                    prev.next = cur.next
                else: 
                    seen.append(cur.val)

            prev = cur
            cur = cur.next
            idx += 1
        return head
