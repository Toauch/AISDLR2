import numpy as np
import matplotlib.pyplot as plt
from binary_tree import BinarySearchTree
from avl_tree import AVLTree
from red_black_tree import RedBlackTree

def plot_tree_height(tree_type, name, color, max_size=10000, step=1000):
    sizes = range(step, max_size + step, step)
    heights = []
    log_heights = []

    for n in sizes:
        # Создаем случайные ключи
        keys = np.random.randint(1, 10000, size=n)
        
        # Создаем и заполняем дерево
        tree = tree_type()
        for key in keys:
            tree.insert(key)
        heights.append(tree.get_height())
        log_heights.append(np.log2(n))

    # Создаем новый график
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, heights, f'{color}-', label=name)
    plt.plot(sizes, log_heights, 'k--', label='log2(n)')

    # Добавляем регрессионный полином
    z = np.polyfit(sizes, heights, 2)
    p = np.poly1d(z)
    plt.plot(sizes, p(sizes), f'{color}:', alpha=0.5, label=f'{name} regression')

    plt.xlabel('Количество ключей')
    plt.ylabel('Высота дерева')
    plt.title(f'Зависимость высоты {name} от количества ключей')
    plt.legend()
    plt.grid(True)
    plt.show()

def print_tree(node, level=0, prefix="Root: "):
    """Вспомогательная функция для визуализации дерева"""
    if not node:
        return
    print("  " * level + prefix + str(node.key))
    if node.left:
        print_tree(node.left, level + 1, "L----")
    if node.right:
        print_tree(node.right, level + 1, "R----")

def demonstrate_trees():
    """Демонстрация всех типов деревьев с одинаковыми значениями"""
    # Фиксированный набор значений
    values = [659, 754, 816, 690, 471, 316, 270, 52, 47, 32]
    
    trees = [
        (BinarySearchTree(), "Binary Search Tree"),
        (AVLTree(), "AVL Tree"),
        (RedBlackTree(), "Red-Black Tree")
    ]
    
    for tree, name in trees:
        print(f"\n{name}")
        print("=" * 50)
        
        # Создаем дерево
        for value in values:
            tree.insert(value)
        
        # Визуализируем структуру
        if isinstance(tree, RedBlackTree):
            print_rb_tree(tree.root, tree.NIL)  # Специальная функция для красно-черного дерева
        else:
            print_tree(tree.root)
        
        # Показываем все типы обходов
        print("\nОбходы дерева:")
        print("-" * 40)
        print(f"Pre-order:    {tree.pre_order()}")
        print(f"In-order:     {tree.in_order()}")
        print(f"Post-order:   {tree.post_order()}")
        print(f"Level-order:  {tree.level_order()}")
        print("-" * 50)

def print_rb_tree(node, NIL, level=0, prefix="Root: "):
    """Специальная функция для визуализации красно-черного дерева"""
    if node == NIL:
        return
    color = "R" if node.color == 1 else "B"
    print("  " * level + prefix + f"{node.key}({color})")
    if node.left != NIL:
        print_rb_tree(node.left, NIL, level + 1, "L----")
    if node.right != NIL:
        print_rb_tree(node.right, NIL, level + 1, "R----")

def test_all_trees():
    # Демонстрация деревьев с фиксированными значениями
    demonstrate_trees()
    
    # Построение графиков
    plot_tree_height(BinarySearchTree, 'Binary Search Tree', 'b')
    plot_tree_height(AVLTree, 'AVL Tree', 'g')
    plot_tree_height(RedBlackTree, 'Red-Black Tree', 'r')

if __name__ == "__main__":
    test_all_trees() 