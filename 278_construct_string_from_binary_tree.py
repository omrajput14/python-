# 278. Construct String from Binary Tree
# Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree2str(root):
    if not root:
        return ""
    res = str(root.val)
    if root.left or root.right:
        res += "(" + tree2str(root.left) + ")"
    if root.right:
        res += "(" + tree2str(root.right) + ")"
    return res

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    print(tree2str(root))  # "1(2(4))(3)"
