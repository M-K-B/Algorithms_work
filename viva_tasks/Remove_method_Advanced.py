def remove(self, target):
    if self.root is None:
        return False
    elif self.root.data == target:
        if self.root.left is None and self.root.right is None:
            self.root = None
        elif self.root.left and self.root.right is None:
            self.root = self.root.left
        elif self.root.left is None and self.root.right:
            self.root = self.root.right
        elif self.root.left and self.root.right:
            delNodeParent = self.root
            delNode = self.root.right

            while delNode.left:
                delNodeParent = delNode
                delNode = delNode.left

            self.root.data = delNode.data
            if delNode.right:
                    if delNodeParent.data > delNode.data:
                       delNodeParent.left = delNode.right
                    elif delNodeParent.data < delNode.data:
                        delNodeParent.right = delNode.right
            else:
                delNodeParent.right = None

    parent = None
    node = self.root

    while node and node.data != target:
        parent = node
        if target < node.data:
            node = node.left
        elif target > node.data:
            node = node.right

    if node is None or node.data != target:
        return False

    elif node.left is None and node.right is None:
        if target < parent.data:
            parent.left = None
        else:
            parent.right = None
        return True

    elif node.left and node.right is None:
        if target < parent.data:
            parent.left = node.left
        else:
            parent.right = node.left
        return True
    
    else:
        delNodeParent = node
        delNode = node.right
        while delNode.left:
            delNodeParent = delNode
            delNode = delNode.left
        
        node.data = delNode.data
        if delNode.right:
            if delNodeParent.data > delNode.data:
                delNodeParent.left = delNode.right
            elif delNodeParent < delNode.data:
                delNodeParent.right = delNode.right
        else:
            if delNode.data < delNodeParent.data:
                delNodeParent.left = None
            else:
                delNodeParent.right = None