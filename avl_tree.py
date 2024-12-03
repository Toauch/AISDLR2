from collections import deque

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance_factor(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        if not node:
            return
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def right_rotate(self, y):
        if not y or not y.left:
            return y
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def left_rotate(self, x):
        if not x or not x.right:
            return x
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def insert(self, key):
        if not self.root:
            self.root = AVLNode(key)
        else:
            self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        # Стандартная вставка BST
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert_recursive(node.left, key)
        elif key > node.key:
            node.right = self._insert_recursive(node.right, key)
        else:
            return node  # Дубликаты не допускаются

        # Обновляем высоту текущего узла
        node.height = 1 + max(self.height(node.left), self.height(node.right))

        # Получаем фактор баланса
        balance = self.balance_factor(node)

        # Случаи балансировки
        # Лево-лево
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Право-право
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Лево-право
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Право-лево
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def get_height(self):
        return self.height(self.root)

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