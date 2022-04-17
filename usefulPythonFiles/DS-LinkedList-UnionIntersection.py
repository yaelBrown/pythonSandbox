from LinkedList import LinkedList
from Node import Node
# Access head_node => list.get_head()
# Check if list is empty => list.is_empty()
# Delete at head => list.delete_at_head()
# Delete by value => list.delete(value)
# Search for element => list.search()
# Length of the list => list.length()
# Remove duplicates => list.remove_duplicates()
# Node class  {int data ; Node next_element;}

# Returns a list containing the union of list1 and list2


def union(list1, list2):
    # Write your code here
    data_ref = []
    out = list1

    current_node = list1.get_head()

    while current_node:
        if current_node.next_element != None:
            current_node = current_node.next_element
        else: 
            current_node.next_element = list2.get_head()
            break

    current_node.remove_duplicates()

    return list1

# Returns a list containing the intersection of list1 and list2


def intersection(list1, list2):
    # Write your code here

    return list1




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
        if(self.is_empty()):
            self.head_node = temp_node
            return self.head_node

        temp_node.next_element = self.head_node
        self.head_node = temp_node
        return self.head_node

    # Inserts a value at the end of the list
    def insert_at_tail(self, value):
        # Creating a new node
        new_node = Node(value)

        # Check if the list is empty, if it is simply point head to new node
        if self.get_head() is None:
            self.head_node = new_node
            return

        # if list not empty, traverse the list to the last node
        temp = self.get_head()

        while temp.next_element is not None:
            temp = temp.next_element

        # Set the nextElement of the previous node to new node
        temp.next_element = new_node
        return

    def length(self):
        # start from the first element
        curr = self.get_head()
        length = 0

        # Traverse the list and count the number of nodes
        while curr is not None:
            length += 1
            curr = curr.next_element
        return length

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

    def delete_at_head(self):
        # Get Head and firstElement of List
        first_element = self.get_head()
        # If List is not empty then link head to the
        # nextElement of firstElement.
        if (first_element is not None):
            self.head_node = first_element.next_element
            first_element.next_element = None
        return

    def delete(self, value):
        deleted = False
        if self.is_empty():  # Check if list is empty -> Return False
            print("List is Empty")
            return deleted
        current_node = self.get_head()  # Get current node
        previous_node = None  # Get previous node
        if current_node.data is value:
            self.delete_at_head()  # Use the previous function
            deleted = True
            return deleted

        # Traversing/Searching for Node to Delete
        while current_node is not None:
            # Node to delete is found
            if value is current_node.data:
                # previous node now points to next node
                previous_node.next_element = current_node.next_element
                current_node.next_element = None
                deleted = True
                break
            previous_node = current_node
            current_node = current_node.next_element

        return deleted

    def search(self, dt):
        if self.is_empty():
            print("List is Empty")
            return None
        temp = self.head_node
        while(temp is not None):
            if(temp.data is dt):
                return temp
            temp = temp.next_element

        print(dt, " is not in List!")
        return None

    def remove_duplicates(self):
        if self.is_empty():
            return

        # If list only has one node, leave it unchanged
        if self.get_head().next_element is None:
            return

        outer_node = self.get_head()
        while outer_node:
            inner_node = outer_node  # Iterator for the inner loop
            while inner_node:
                if inner_node.next_element:
                    if outer_node.data == inner_node.next_element.data:
                        # Duplicate found, so now removing it
                        new_next_element = inner_node.next_element.next_element
                        inner_node.next_element = new_next_element
                    else:
                        # Otherwise simply iterate ahead
                        inner_node = inner_node.next_element
                else:
                    # Otherwise simply iterate ahead
                    inner_node = inner_node.next_element
            outer_node = outer_node.next_element
        return






class Soln:
    def union(list1, list2):
    # Return other List if one of them is empty
        if (list1.is_empty()):
            return elements(list2)
        elif (list2.is_empty()):
            return elements(list1)

        start = list1.get_head()

        # Traverse the first list till the tail
        while start.next_element:
            start = start.next_element

        # Link last element of first list to the first element of second list
        start.next_element = list2.get_head()
        list1.remove_duplicates()
        return list1


    def intersection(list1, list2):

        result = LinkedList()
        visited_nodes = set()  # Keep track of all the visited nodes
        current_node = list1.get_head()

        # Traversing list1 and adding all unique nodes into the hash set
        while current_node:
            value = current_node.data
            if value not in visited_nodes:
                visited_nodes.add(value)  # Visiting current_node for first time
            current_node = current_node.next_element

        start = list2.get_head()

        # Traversing list 2
        # Nodes which are already present in visited_nodes are added to result
        while start:
            value = start.data
            if value in visited_nodes:
                result.insert_at_head(start.data)
            start = start.next_element
        result.remove_duplicates()
        return result