class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, root):
        if not root:
            return 0
        return root.height
    
    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)
    
    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        
        return x
    
    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        
        return y
    
    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
            
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)
        
        # LL Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        # RR Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        # LR Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        # RL Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
            
        return root

    def pre_order(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.pre_order(root.left)
        self.pre_order(root.right)

if __name__ == "__main__":
    myTree = AVLTree()
    root = None

    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = myTree.insert(root, key)
        
    print("Preorder traversal of the constructed AVL tree is:")
    myTree.pre_order(root)
    print()
