# 270. Binary Tree Tilt
# Given the root of a binary tree, return the sum of every tree node's tilt.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.total_tilt = 0
        
    def findTilt(self, root):
        def value_sum(node):
            if not node:
                return 0
            left_sum = value_sum(node.left)
            right_sum = value_sum(node.right)
            tilt = abs(left_sum - right_sum)
            self.total_tilt += tilt
            return node.val + left_sum + right_sum
            
        value_sum(root)
        return self.total_tilt

if __name__ == "__main__":
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    sol = Solution()
    print(sol.findTilt(root))  # 1
