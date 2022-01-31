def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:       
    prev = None
    cur = head
    next = None
    
    while cur: 
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
        
    return prev