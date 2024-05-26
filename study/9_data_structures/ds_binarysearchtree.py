class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val
    
    def insert(self, val):
        if self.val == None:
            self.val = val
        if self.val == val:
            pass
        if val < self.val and self.left == None:
            self.left = BSTNode(val)
        if val < self.val and self.left:
            self.left.insert(val)
        if val > self.val and self.right == None:
            self.right = BSTNode(val)
        if val > self.val and self.right:
            self.right.insert(val)

    def get_min(self):
        if self.left is None:
            return self.val
        else:
            return self.left.get_min()
        
    def get_max(self):
        if self.right is None:
            return self.val
        else:
            return self.right.get_max()
