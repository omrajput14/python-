# 314. Binary Tree Vertical Order Traversal
# Given the root of a binary tree, return the vertical order traversal of its nodes' values.

from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_order(root):
    if not root: return []
    column_table = defaultdict(list)
    queue = deque([(root, 0)])
    
    while queue:
        node, column = queue.popleft()
        column_table[column].append(node.val)
        if node.left: queue.append((node.left, column - 1))
        if node.right: queue.append((node.right, column + 1))
        
    return [column_table[x] for x in sorted(column_table.keys())]

if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(vertical_order(root))
