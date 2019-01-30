from collections.abc import Iterable 


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right =  None
        self.parent = None
    
    def insert(self, data):
        if self.val:
            if data < self.val:
                if self.left is None:
                    self.left = Node(data)
                    self.left.parent = self
                else:
                    self.left.insert(data)
            elif data > self.val:
                if self.right is None:
                    self.right = Node(data)
                    self.right.parent = self
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def disconnect(self):
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self, nums=None):
        # nums must be an Iterable object
        if nums:
            if isinstance(nums, Iterable):
                self.root = Node(nums[0])
                if len(nums)>1:
                    for num in nums[1:]:
                        self.root.insert(num)
            else:
                raise Exception('@nums must be an Iterable')    
        else:
            self.root = None 
    def inorder_print(self):
        #inorder print
        def inorder(root):
            if root:
                if root.left:
                    inorder(root.left)
                print(root.val)
                if root.right:
                    inorder(root.right)
        inorder(self.root)

    
    def insert(self, val):
        tree_insert(self, Node(val))
    
    def delete(self, val):
        node = tree_search(self.root, val)
        tree_delete(self, node)

    def search(self, val):
        return tree_search(self.root, val)
    
    def minimum(self, val):
        return find_min(self.root)
    
    def maxinum(self, val):
        return find_max(self.root)
    
    
def tree_search(root, key):
    '''
    @param root: Node
    @param key: key
    '''
    node = root
    while not node and key != node.val:
        if key < node.val:
            node = node.left
        else:
            node = node.right
    return node 

def find_min(root):
    '''
    @root: the root of a BST
    '''
    while root.left:
        root = root.left
    return root

def find_max(root):
    while root.right:
        root = root.right
    return root

def find_next_larger(node):
    if node.right:
        return find_min(node.right)
    parent = node.parent
    while parent and node == parent.right:
        node = parent
        parent = node.parent
    return parent

def find_next_smaller(node):
    if node.left:
        return find_max(node.left)
    parent = node.parent
    while parent and node == parent.left:
        node = parent
        parent = node.parent
    return parent

def tree_insert(tree, node):
    y = None
    x = tree.root
    while x:
        y = x
        if node.val < x.val:
            x = x.left
        else:
            x = x.right
    node.parent = y
    if not y:
        tree.root = node
    elif node.val < y.val:
        y.left = node
    else:
        y.right = node

def transplant(tree, u, v):
    '''
    @tree: bst
    @u: a node in bst
    @v: a node in bst
    '''
    if not u.parent:
        tree.root = v
    elif u == u.parent.left:
        u.parent.left = v
    elif u == u.parent.right:
        u.parent.right = v
    if not v:
        v.parent = u.parent
    
def tree_delete(tree, node):
    '''
    @tree: bst
    @node: the node will be deleted
    '''
    if not node.left:
        transplant(tree, node, node.right)
    elif not node.right:
        transplant(tree, node, node.left)
    else:
        y = find_min(node.right)
        if y.parent != node:
            transplant(tree, y, y.right)
            y.right = node.right
            y.right.parent = y
        transplant(tree, node, y)
        y.left = node.left
        y.left.parent = y


