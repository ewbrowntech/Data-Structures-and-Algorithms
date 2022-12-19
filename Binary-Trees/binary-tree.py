"""
binary-tree.py
@Author - Ethan Brown - ewbrowntech@gmail.com
@Version - 18 DEC 22

Implementation of a basic binary tree in Python
"""


# TreeNode object has attributes:
# - value: value stored within the node
# - left: left branch extending from the node
# - right: right branch extending from the node
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# ------------------------------
# Printing a tree
# ------------------------------
def print_tree(root, level=0):
    if root is not None:
        print_tree(root.right, level + 1)
        print(' ' * 4 * level + '==', root.value)
        print_tree(root.left, level + 1)


# ------------------------------
# Example
# ------------------------------
binary_tree = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(6, TreeNode(7), TreeNode(8)))
print_tree(binary_tree)
