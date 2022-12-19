from Binary_Trees.binary_tree import TreeNode, print_tree
from Binary_Trees.binary_tree_traversals import level_order_traversal, inorder_traversal, preorder_traversal, postorder_traversal

binary_tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print("Tree: ")
print_tree(binary_tree)

# ------------------------------
# Level-Order Traversal (Breadth-First)
# ------------------------------
print("Level Order Traversal:", end=' ')
level_order_traversal(binary_tree)  # 1 2 3 4 5 6 7

# ------------------------------
# Inorder Traversal (Depth First)
# ------------------------------
print("\n\nInorder Traversal: ", end=' ')
inorder_traversal(binary_tree)  # 4 2 5 1 6 3 7

# ------------------------------
# Preorder Traversal (Depth First)
# ------------------------------
print("\n\nPreorder Traversal:", end=' ')
preorder_traversal(binary_tree)  # 1 2 4 5 3 6 7

# ------------------------------
# Postorder Traversal (Depth First)
# ------------------------------
print("\n\nPostorder Traversal:", end=' ')
postorder_traversal(binary_tree)  # 4 5 2 6 7 3 1

