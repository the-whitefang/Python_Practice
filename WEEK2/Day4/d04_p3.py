'''
Binary Tree in Python
it has three types of traversal:
1. Preorder -> root--Left--Right
2. Postorder -> left--right--root
3. Inorder ->  left--root--right
'''

class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

def Inorder(root):
    if root:
        Inorder(root.left)
        print(str(root.val) + "->", end =' ')
        Inorder(root.right)

def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(str(root.val) + "->", end=" ")

def Preorder(root):
    if root:
        print(str(root.val) + "->", end=" ")
        Preorder(root.left)
        Preorder(root.right)

root=Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Inorder Traversal:")
Inorder(root)
print("\nPreorder Traversal")
Preorder(root)
print("\nPostorder Traversal")
Postorder(root)


