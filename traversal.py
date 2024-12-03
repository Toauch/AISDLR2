from collections import deque

def add_traversal_methods(tree_class):
    def dfs_inorder(self, node, result):
        if node:
            self.dfs_inorder(node.left, result)
            result.append(node.key)
            self.dfs_inorder(node.right, result)
        return result

    def bfs(self):
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

    tree_class.dfs_inorder = lambda self: dfs_inorder(self, self.root, [])
    tree_class.bfs = bfs 