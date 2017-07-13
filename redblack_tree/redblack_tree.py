#!/usr/bin/env python3

class Node:
    '''Red/black Node'''
    def __init__(self, value, color='red'):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = color
    @property
    def color(self):
        return self._color
    @color.setter
    def color(self, x):
        x = x.lower()
        if x not in ['red', 'black']:
            raise ValueError('%s is not a valid color.' % x)
        self._color = x
    def __repr__(self):
        return str(self.value)
    
class RedBlackTree:
    '''Red/black tree class'''
    def __init__(self):
        self.root = None

    def _insert(self, value):
        '''Insert new node into RB tree'''
        if self.root is None:
            self.root = Node(value, color='black')

    def _inOrder(self, current):
        if current is not None:
            yield from self._inOrder(current.left)
            yield current
            yield from self._inOrder(current.right)

    def insert(self, value):
        self._insert(value)

    def inOrder(self):
        '''in-Order traversal generator'''
        return self._inOrder(self.root)
