#!/usr/bin/env python3
'''Simple binary tree with traversal'''

class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.key)
        

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def _insert(self, value, current):
        '''recursively traveses tree to add new node'''
        if value > current.key:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert(value, current.right)
        else:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert(value, current.left)
    
    def _delete(self, value, current, parent=None):
        '''recursive method that walks tree looking for node to delete'''
        if current.key == value:
            # case 1: leaf, change parent left/right to None
            if current.left is None and current.right is None:
                if parent is None:
                    self.root = None
                else:
                    if parent.left is not None:
                        if parent.left.key == current.key:
                            parent.left = None
                    if parent.right is not None:
                        if parent.right.key == current.key:
                            parent.right = None
            # case 2: one child, move up child
            elif current.left is None:
                current.key = current.right.key
                current.left = current.right.left
                current.right = current.right.right
            elif current.right is None:
                current.key = current.left.key
                current.left = current.left.left
                current.right = current.left.right
            # case 3: two children, replace current with min from right subtree
            else:
                min_max = self._localMin(current.right)
                current.key = min_max
                self._delete(min_max, current.right, current) 
        elif value > current.key:
            self._delete(value, current.right, current)
        else:
            self._delete(value, current.left, current) 

    def _localMin(self, current):
        # Find min of subtree
        if current.left is None:
            return current.key
        else:
            return self._localMin(current.left)

    def _inOrder(self, current):
        '''in-order tree traversal'''
        if current is not None:
            yield from self._inOrder(current.left)
            yield current
            yield from self._inOrder(current.right)

    def _preOrder(self, current):
        '''pre-order tree traversal'''
        if current is not None:
            yield current
            yield from self._preOrder(current.left)
            yield from self._preOrder(current.right)
                

    def _postOrder(self, current):
        '''pre-order tree traversal'''
        if current is not None:
            yield from self._postOrder(current.left)
            yield from self._postOrder(current.right)
            yield current
    
    def _search(self, value, current):
        '''recursive search through tree'''
        if current is None:
            return False
        elif current.key == value:
            return True
        elif value > current.key:
            return self._search(value, current.right)
        else:
            return self._search(value, current.left) 

    def insert(self, value):
        '''public api for add method'''
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def inOrder(self):
        '''in-order tree traversal'''
        return self._inOrder(self.root)

    def preOrder(self):
        '''pre-order tree traversal'''
        return self._preOrder(self.root)

    def postOrder(self):
        '''post-order tree traversal'''
        return self._postOrder(self.root)

    def search(self, value):
        if self.root.key == value:
            return True
        else:
            return self._search(value, self.root)

    def delete(self, value):
        '''Delete node from tree'''
        if not self.search(value):
            raise ValueError
        self._delete(value, self.root)
            
    
if __name__ == "__main__":
    # create tree
    print("Creating tree...")
    bt = BinaryTree()
    values = [4, 2, 6, 1, 7, 3, 5]
    print("values: ", values)
    for v in values: bt.insert(v)
    # traverse tree
    print("Traversals...")
    print("in-order: ",  list(bt.inOrder()))
    print("pre-order: ", list(bt.preOrder()))
    print("post-order: ", list(bt.postOrder()))
    # search tree
    print("Search...")
    for v in [4, 6, 10]: 
        if bt.search(v):
            print("%s in tree" % v)
        else:
            print("%s not in tree" % v)
    # deletion
    print("Deletion...")
    for v in [1, 2, 4]:
        print("deleting: ", v)
        bt.delete(v)
        print("in-order: ", list(bt.inOrder()))
        
