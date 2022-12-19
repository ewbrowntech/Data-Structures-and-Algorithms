from collections import deque
"""
binary_tree_traversals.py
@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 18 DEC 22

Implementation of breadth-first and depth-first traversals of binary trees
"""


# ------------------------------
# Breadth-First Traversal
# ------------------------------
def level_order_traversal(root):
    if not root:
        return
    queue = deque()  # A double-ended queue is used here as it allows us to quickly remove items
                     # (nodes in this case) from the left-most position of the queue
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(node.value, end=' ')
        if node.left: queue.append(node.left)  # Level-ordering achieved by sequentially appending all nodes on layer
        if node.right: queue.append(node.right)


# ------------------------------
# Depth-First Traversal
# ------------------------------
# Analyzes left branch, then root, then right branch
def inorder_traversal(root):
    if not root:
        return
    inorder_traversal(root.left)
    print(root.value, end=' ')
    inorder_traversal(root.right)

# Analyzes root, then left branch, then right branch
# Useful for copying a tree or obtaining a prefix expression
def preorder_traversal(root):
    if not root:
        return
    print(root.value, end=' ')
    preorder_traversal(root.left)
    preorder_traversal(root.right)

# Analyzes left branch, then right branch, then root
# Useful for deleting a tree or obtaining a postfix expression
def postorder_traversal(root):
    if not root:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.value, end=' ')
