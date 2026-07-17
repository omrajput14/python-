# 279. Merge Two Binary Trees
# You are given two binary trees root1 and root2. Merge them into a new binary tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def merge_trees(root1, root2):
    if not root1 and not root2:
        return None
    if not root1:
        return root2
    if not root2:
        return root1
        
    root = TreeNode(root1.val + root2.val)
    root.left = merge_trees(root1.left, root2.left)
    root.right = merge_trees(root1.right, root2.right)
    return root

if __name__ == "__main__":
    r1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    r2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
    merged = merge_trees(r1, r2)
    print(merged.val)  # 3
