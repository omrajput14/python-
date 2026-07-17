# 272. Subtree of Another Tree
# Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_subtree(root, subRoot):
    def is_match(s, t):
        if not s and not t: return True
        if not s or not t: return False
        return s.val == t.val and is_match(s.left, t.left) and is_match(s.right, t.right)
        
    if not root: return False
    if is_match(root, subRoot): return True
    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    sub = TreeNode(4, TreeNode(1), TreeNode(2))
    print(is_subtree(root, sub))  # True
