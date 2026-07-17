# 285. Second Minimum Node In a Binary Tree
# Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root):
        res = [float('inf')]
        min_val = root.val
        
        def dfs(node):
            if not node:
                return
            if min_val < node.val < res[0]:
                res[0] = node.val
            elif node.val == min_val:
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)
        return res[0] if res[0] != float('inf') else -1

if __name__ == "__main__":
    root = TreeNode(2, TreeNode(2), TreeNode(5, TreeNode(5), TreeNode(7)))
    sol = Solution()
    print(sol.findSecondMinimumValue(root))  # 5
