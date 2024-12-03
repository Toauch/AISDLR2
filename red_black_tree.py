from collections import deque

class Color:
    RED = 1
    BLACK = 0

class RBNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = Color.RED

class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None)
        self.NIL.color = Color.BLACK
        self.root = self.NIL

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = RBNode(key)
        node.left = self.NIL
        node.right = self.NIL
        
        y = None
        x = self.root
        
        while x != self.NIL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right
        
        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node
            
        self._fix_insert(node)

    def _fix_insert(self, k):
        while k.parent and k.parent.color == Color.RED:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == Color.RED:
                    u.color = Color.BLACK
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == Color.RED:
                    u.color = Color.BLACK
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = Color.BLACK
                    k.parent.parent.color = Color.RED
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = Color.BLACK

    def get_height(self):
        return self._get_height_recursive(self.root)
    
    def _get_height_recursive(self, node):
        if node == self.NIL:
            return 0
        return 1 + max(self._get_height_recursive(node.left),
                      self._get_height_recursive(node.right))

    def bfs(self):
        """Обход в ширину"""
        if self.root == self.NIL:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.key)
            
            if node.left != self.NIL:
                queue.append(node.left)
            if node.right != self.NIL:
                queue.append(node.right)
                
        return result

    def dfs_inorder(self):
        """Обход в глубину (in-order)"""
        result = []
        self._dfs_inorder_recursive(self.root, result)
        return result
    
    def _dfs_inorder_recursive(self, node, result):
        if node != self.NIL:
            self._dfs_inorder_recursive(node.left, result)
            result.append(node.key)
            self._dfs_inorder_recursive(node.right, result)

    def pre_order(self):
        """Прямой обход (корень->лево->право)"""
        result = []
        def traverse(node):
            if node != self.NIL:
                result.append(node.key)
                traverse(node.left)
                traverse(node.right)
        traverse(self.root)
        return result

    def in_order(self):
        """Симметричный обход (лево->корень->право)"""
        result = []
        def traverse(node):
            if node != self.NIL:
                traverse(node.left)
                result.append(node.key)
                traverse(node.right)
        traverse(self.root)
        return result

    def post_order(self):
        """Обратный обход (лево->право->корень)"""
        result = []
        def traverse(node):
            if node != self.NIL:
                traverse(node.left)
                traverse(node.right)
                result.append(node.key)
        traverse(self.root)
        return result

    def level_order(self):
        """Обход по уровням"""
        if self.root == self.NIL:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.key)
            
            if node.left != self.NIL:
                queue.append(node.left)
            if node.right != self.NIL:
                queue.append(node.right)
                
        return result