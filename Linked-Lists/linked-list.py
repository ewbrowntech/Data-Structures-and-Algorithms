'''
linked-list.py
@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 17 DEC 22

Implementing a basic linked list structure in Python.
Contains a simple example program.
'''

# Node object has attributes:
# - data: This is the data contained within a node of a linked list, such as a string, number, or another object
# - next: This is a pointer to the next node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List object has attributes:
# - head: The pointer to the first node in the list
class LinkedList:
    def __init__(self):
        self.head = None

    # append() - append a new node to the end of a linked list
    # Parameters:
    # - self: The linked list to which the node will be appended
    # - data: The data to be stored in the new node
    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # If the linked list is empty, place a new node at the head to start one
            self.head = new_node
            return
        current = self.head
        while current.next is not None:  # Traverse the linked list, as new nodes must be place at the end
            current = current.next
        current.next = new_node  # Place the new node at the end of the linked list

    # remove() - delete the first node in the linked list containing specified data
    # Parameters:
    # - self: The linked list from which a matching node will be removed
    # - data: The data a node must contain to qualify for removal
    def remove(self, data):
        current = self.head
        if current is not None and current.data == data:  # If a hit is found at the head, move the head forward one element
            self.head = current.next
            current = None
            return
        previous = None
        while current is not None and current.data != data:  # Traverse the linked list until a match is found
            previous = current
            current = current.next
        if current is None:  # If traversal reaches the end of the list before a match is found, then there is a no node
            return           # containing the specified data
        previous.next = current.next
        current = None  # If a match was found, remove the node containing the specified data

# Purely for example purposes
def print_list(linked_list):
    outputString = ""
    current = linked_list.head
    while current is not None:
        if current.next is not None: outputString += current.data + " - "
        else: outputString += current.data
        current = current.next
    print(outputString)

# ------------------------------
# Driver
# ------------------------------

linked_list = LinkedList()

linked_list.append("This")
linked_list.append("is")
linked_list.append("a")
linked_list.append("linked")
linked_list.append("list")
linked_list.append("probably")
print_list(linked_list)

linked_list.remove("probably")
print_list(linked_list)
