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


# def detect_loop(lst):
#     if lst.is_empty():
#         return False

#     start = cur = lst.get_head()
#     cnt = 0

#     while cur:
#         print(cnt)
#         if cnt > 0: 
#             if cur == start:
#                 return True
#         cnt += 1
#         cur = cur.next_element

#     return False

# Floyd's Cycle Finding Algorithm
def detect_loop(lst):
    # Keep two iterators
    one_step = lst.get_head()
    two_step = lst.get_head()
    while one_step and two_step and two_step.next_element:
        one_step = one_step.next_element  # Moves one node at a time
        two_step = two_step.next_element.next_element  # skips a node
        if one_step == two_step:  # Loop exists
            return True
    return False