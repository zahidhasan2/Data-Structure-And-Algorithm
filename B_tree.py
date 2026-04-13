
## Python Implementation
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Example Tree:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

# DFS Traversals(Recursion)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.value, end=" ")
        inorder(node.right)        
def preorder(node):
    if node:
        print(node.value, end=" ")
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        print(node.value, end=" ")

# BFS Traversal (Level-order)
from collections import deque

def level_order(node):
    result=[]
    queue = deque([])
    queue.append(node)
    while len(queue)!=0:
        cur = queue.popleft()
        result.append(cur.value)
        
        if cur.left is not None:
            queue.append(cur.left)
        if cur.right is not None:
            queue.append(cur.right)
    return result        

# Function to count leaf nodes
def count_leaves(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return count_leaves(node.left) + count_leaves(node.right)

# Testing
print("Inorder Traversal:")
inorder(root)
print("\nPreorder Traversal:")
preorder(root)
print("\nPostorder Traversal:")
postorder(root)
print("\nLevel-order Traversal:")
level_order(root)
print(f"\nNumber of leaf nodes: {count_leaves(root)}")