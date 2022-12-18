'''
sparse-array.py
@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 17 DEC 22

Representing a sparse array (one in which one or many values are null or identical) in the form of a linked list
'''

'''
Approach:
For each sequence of adjacent values in a sparse array, say the subset S = [1, 1, 1] in the sparse array 
A = [1, 1, 1, 2, None, 3], append to the linked list a new node containing the index at which the first value of S 
appears in A (0), the value itself (1), and the length of subset S (3). Ignore all elements of A containing no data (4).

To reconstruct the sparse array from the linked list, traverse the linked list. For each node in the linked list append 
the node's value to the array node.count times, while making sure to append the specified null value (EX: None) at each
index not covered comprising a node in the linked list.
'''

class Node:
    def __init__(self, index, value, count):
        self.index = index
        self.value = value
        self.count = count
        self.next = None

# A linked list representing a sparse array
class CollapsedSparseArray:
    def __init__(self):
        self.head = None

    # Create a node for every subset of adjacent identical values in the sparse array, while ignore null values
    def create_node(self, index, value):
        if value == None:  # Do not store blank/default values (None is just an example here but could be 0, null, etc.)
            return
        if self.head is None:  # If the linked list is empty, use the first valid value to create the first node
            self.head = Node(index, value, 1)
            return
        current = self.head

        while current is not None and current.next is not None:
            current = current.next
        if current.value == value:  # Compare specified value against that stored in the last node of the linked list
            current.count += 1      # If they are the same, increment the count of that node
        else:
            new_node = Node(index, value, 1)
            current.next = new_node  # Otherwise, append a new node containing that value

# Convert sparse array (list) into linked list representation
def collapse_sparse_array(sparse_array):
    linked_list = CollapsedSparseArray()
    for i, value in enumerate(sparse_array):
        linked_list.create_node(i, value)
    return linked_list

# Reconstruct the original sparse array from linked list representation
def construct_sparse_array(linked_list):
    sparse_array = []
    current = linked_list.head
    while current is not None:
        while current.index > len(sparse_array):  # For all indices not comprising a node, append null value (EX: None)
            sparse_array.append(None)
        sparse_array.extend([current.value] * current.count)
        current = current.next
    return sparse_array

# Format linked list into next output (purely for demonstration purposes)
def format_list(converted_sparse_array):
    outputString = ""
    current = converted_sparse_array.head
    while current is not None:
        if current.next is not None: outputString += "(" + str((current.index, current.value, current.count)) + ") - "
        else: outputString += "(" + str((current.index, current.value, current.count)) + ")"
        current = current.next
    return outputString

# ------------------------------
# Driver
# ------------------------------
sparse_array = [None, None, 1, 1, 1, 2, 3, None, 1, 1]
print("Original Sparse Array: " + str(sparse_array))
collapsed_sparse_array = collapse_sparse_array(sparse_array)
print("Converted Sparse Array: " + format_list(collapsed_sparse_array))
reconstructed_sparse_array = construct_sparse_array(collapsed_sparse_array)
print("Reconstructed Sparse Array: " + str(reconstructed_sparse_array))

