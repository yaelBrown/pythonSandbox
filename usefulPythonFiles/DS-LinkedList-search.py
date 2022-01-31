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

    # Supplementary print function
    def print_list(self):
        if(self.is_empty()):
            print("List is Empty")
            return False
        temp = self.head_node
        while temp.next_element is not None:
            print(temp.data, end=" -> ")
            temp = temp.next_element
        print(temp.data, "-> None")
        return True

class Node:
    def __init__(self, data):
        self.data = data
        self.next_element = None

# def search(lst, value):
#     # Write your code here
#     temp = lst.get_head()
#     while temp.next_element: 
#         if temp.data is value:
#             return True
#         else: 
#             temp = temp.next_element
    
#     return False


def search(lst, value):

    # Start from first element
    current_node = lst.get_head()

    # Traverse the list till you reach end
    while current_node:
        if current_node.data == value:
            return True  # value found
        current_node = current_node.next_element
    return False  # value not found
