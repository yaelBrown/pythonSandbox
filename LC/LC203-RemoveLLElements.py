# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None: return head
        cur = head
        prev = ListNode()
        while cur:
            if cur.val == val:
                prev.next = cur.next
            prev = cur
            cur = cur.next

        return head
    
# does not work for ll == [7,7,7,7] 
#   returns [7,7]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None: return head
        prev = ListNode(0)

        while head and head.val == val:
            print("xx")
            head = head.next

        cur = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            prev = cur
            cur = cur.next

        return head
    






# "Easy beginner solution"


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev ,curr = dummy, head

        while curr:
            if curr.val == val:
                curr = curr.next
                prev.next = curr
            else:
                curr =curr.next
                prev = prev.next
            

        return dummy.next