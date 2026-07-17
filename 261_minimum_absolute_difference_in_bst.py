# 261. Minimum Absolute Difference in BST
# Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_minimum_difference(root):
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    vals = inorder(root)
    min_diff = float('inf')
    for i in range(1, len(vals)):
        min_diff = min(min_diff, vals[i] - vals[i-1])
        
    return min_diff

if __name__ == "__main__":
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
    print(get_minimum_difference(root))  # 1
