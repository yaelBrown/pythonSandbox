class Node:
  def __init__(self, data):
    self.data = data
    self.next_element = None

class LinkedList:
    def __init__(self):
        self.head_node = None

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if(self.head_node is None):  # Check whether the head is None
            return True
        else:
            return False

    def insert_at_head(self, dt):
        temp_node = Node(dt)
        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node


# def find_mid(lst):
#     if lst.is_empty():
#         return False

#     mid = (lst.length() / 2)
#     idx = 0
#     cur = lst.get_head()

#     while cur:
#         if idx is mid: 
#             return cur
#         idx += 1
#         cur.next_element

def find_mid(lst):
    if lst.is_empty():
        return -1
    current_node = lst.get_head()
    if current_node.next_element is None:
        # Only 1 element exist in array so return its value.
        return current_node.data

    mid_node = current_node
    current_node = current_node.next_element.next_element
    # Move mid_node (Slower) one step at a time
    # Move current_node (Faster) two steps at a time
    # When current_node reaches at end, mid_node will be at the middle of List
    while current_node:
        mid_node = mid_node.next_element
        current_node = current_node.next_element
        if current_node:
            current_node = current_node.next_element
    if mid_node:
        return mid_node.data
    return -1

# Brute Force
# def find_mid(lst):
#     if lst.is_empty():
#         return None

#     node = lst.get_head()
#     mid = 0
#     if lst.length() % 2 == 0:
#         mid = lst.length()//2
#     else:
#         mid = lst.length()//2 + 1

#     for i in range(mid - 1):
#         node = node.next_element

#     return node.data