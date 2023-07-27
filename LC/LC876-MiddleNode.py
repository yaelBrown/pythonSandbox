# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        # cnt
        cnt = 0
        cur = head
        while cur:
            cnt += 1
            cur = cur.next

        # find and return idx
        isEven = cnt % 2 == 0
        t = (cnt / 2)
        mid = (int(t)) if t % 2 != 0 else (t + 1)

        print(f"mid: {mid}\ncnt: {cnt}\nisEven: {isEven}")
        cur = head
        while head: 
            head = head.next
            cnt -= 1

            if cnt == mid + 1:
                if not isEven:
                    cur = head
                    return cur
                else:
                    return head.next