# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        temp = ""

        while cur:
            temp += str(cur.val)
            cur = cur.next

        return temp == temp[::-1]
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # cur = head
        # temp = ""

        # while cur:
        #     temp += str(cur.val)
        #     cur = cur.next

        # return temp == temp[::-1]
        
        slow = fast = head

        while fast:
            fast = fast.next.next
            slow = slow.next

        prev = None
        cur = slow
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

        l1 = head
        l2 = prev
        while l2:
            if l1.val != l2.val:
                return False
            l1 = l1.next
            l2 = l2.next

        return True