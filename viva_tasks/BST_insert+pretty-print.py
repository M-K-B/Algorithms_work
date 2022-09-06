""" Basic BST code for inserting (i.e. building) and printing a tree

    Your ***first standard viva task*** (of 5) will be to implement a find method into
    the class BinaryTree from pseudocode. See the lab task sheet for Week 4. 

    Your ***first advanced viva task*** (of 3) will be to implement a remove (delete) method
    into the class Binary Tree from partial pseudocode. See the lab task sheet for Week 4.

    Since the given code is in python it is strongly suggested you stay with python; but
    if you want to reimplement as C++ this is also OK (but not worth extra credit)
"""

import math

""" Node class
"""

class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

""" BST class with insert and display methods. display pretty prints the tree
"""

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
            else:
                self._insert(data, cur_node.left)
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value already present in tree")






    def display(self, cur_node):
        lines, _, _, _ = self._display(cur_node)
        for line in lines:
            print(line)

    def _display(self, cur_node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if cur_node.right is None and cur_node.left is None:
            line = '%s' % cur_node.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if cur_node.right is None:
            lines, n, p, x = self._display(cur_node.left)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if cur_node.left is None:
            lines, n, p, x = self._display(cur_node.right)
            s = '%s' % cur_node.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self._display(cur_node.left)
        right, m, q, y = self._display(cur_node.right)
        s = '%s' % cur_node.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


    def find_i(self, target):  # Find interatively 
        cur_node = self.root
        while cur_node != None:
            if cur_node.data == target: 
                return True
            elif cur_node.data > target:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return False

    ''''''
    def find_r(self, target):   # Find recursively
        if self.root:                                           # root has value
            if self._find_r(target,self.root):
                return True
            return False
        else:
            return None
    
    def _find_r(self, target, cur_node):
        if target > cur_node.data and cur_node.right:
            return self._find_r(target, cur_node.right)
        elif target < cur_node.data and cur_node.left:
            return self._find_r(target, cur_node.left)
        if target == cur_node.data:
            return True

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

        
bst = BinaryTree()
bst.insert(4)
bst.insert(2)
bst.insert(6)
bst.insert(1)
bst.insert(3)
bst.insert(5)
bst.insert(7)

##bst.insert(8)
##bst.insert(9)
##bst.insert(10)
##bst.insert(11)
##bst.insert(12)
##bst.insert(13)
##bst.insert(14)
##bst.insert(15)
##bst.insert(100)
##bst.insert(200)


bst.display(bst.root)



print(bst.find_i(3))
print(bst.find_r(3))

print(bst.remove(3))

bst.display(bst.root)
