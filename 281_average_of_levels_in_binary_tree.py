# 281. Average of Levels in Binary Tree
# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def average_of_levels(root):
    if not root:
        return []
        
    res = []
    q = deque([root])
    
    while q:
        level_sum = 0
        level_len = len(q)
        for _ in range(level_len):
            node = q.popleft()
            level_sum += node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(level_sum / level_len)
        
    return res

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(average_of_levels(root))  # [3.0, 14.5, 11.0]
