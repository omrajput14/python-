# Binary Search Tree (BST) Example
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

if __name__ == "__main__":
    r = Node(50)
    insert(r, 30)
    insert(r, 20)
    insert(r, 40)
    insert(r, 70)
    insert(r, 60)
    insert(r, 80)
    print("Inorder traversal of the given tree:")
    inorder(r)
    print()
