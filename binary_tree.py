from collections import deque

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)
    
    def _insert_recursive(self, node, key):
        if not node:
            return Node(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        else:
            node.right = self._insert_recursive(node.right, key)
        return node

    def search(self, key):
        return self._search_recursive(self.root, key)
    
    def _search_recursive(self, node, key):
        if not node or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def get_height(self):
        return self._get_height_recursive(self.root)
    
    def _get_height_recursive(self, node):
        if not node:
            return 0
        return 1 + max(self._get_height_recursive(node.left),
                      self._get_height_recursive(node.right)) 

    def bfs(self):
        """Обход в ширину"""
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.key)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return result

    def dfs_inorder(self):
        """Обход в глубину (in-order)"""
        result = []
        self._dfs_inorder_recursive(self.root, result)
        return result
    
    def _dfs_inorder_recursive(self, node, result):
        if node:
            self._dfs_inorder_recursive(node.left, result)
            result.append(node.key)
            self._dfs_inorder_recursive(node.right, result)

    def pre_order(self):
        """Прямой обход (корень->лево->право)"""
        result = []
        def traverse(node):
            if node:
                result.append(node.key)
                traverse(node.left)
                traverse(node.right)
        traverse(self.root)
        return result

    def in_order(self):
        """Симметричный обход (лево->корень->право)"""
        result = []
        def traverse(node):
            if node:
                traverse(node.left)
                result.append(node.key)
                traverse(node.right)
        traverse(self.root)
        return result

    def post_order(self):
        """Обратный обход (лево->право->корень)"""
        result = []
        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                result.append(node.key)
        traverse(self.root)
        return result

    def level_order(self):
        """Обход по уровням"""
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.key)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        return result