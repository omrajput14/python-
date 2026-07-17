# 265. Diameter of Binary Tree
# Given the root of a binary tree, return the length of the diameter of the tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0
        
    def diameterOfBinaryTree(self, root):
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1
            
        depth(root)
        return self.diameter

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    sol = Solution()
    print(sol.diameterOfBinaryTree(root))  # 3
