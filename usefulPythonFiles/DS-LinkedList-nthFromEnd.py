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

# Function to find the nth node from end of Linked List


def find_nth(lst, n):
    # Write your code here

    len = lst.length()
    if n > len:
        return -1
    if n is len:
        return lst.get_head()

    idx = len - n

    current_node = lst.get_head()
    cnt = 0

    while current_node.next_element: 
        if cnt is idx:
            return current_node.data
        else: 
            cnt += 1
            current_node = current_node.next_element


