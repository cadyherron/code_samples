"""
Serialize binary tree to/from string
"""


class BinaryTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return BinaryTreeNode(value)
    else:
        if root.value == value:
            return root
        if root.value < value:
            root.right = insert(root.right, value)
        else:
            root.left = insert(root.left, value)
    return root


def build_tree():
    tree = BinaryTreeNode(50)
    tree = insert(tree, 56)
    tree = insert(tree, 6)
    tree = insert(tree, 78)
    tree = insert(tree, 14)
    tree = insert(tree, 15)
    tree = insert(tree, 87)
    tree = insert(tree, 43)
    tree = insert(tree, 4)
    tree = insert(tree, 15)
    return tree


def print_tree(tree):
    # let's do breadth first search
    # FIFO with a queue, append and .pop(0)
    # with a balanced tree, the number of nodes would double with each level
    depth = 0
    queue = [(tree, depth)]
    stuff_to_print = {}
    # {0: [1], 1: [5,6,7,8]}
    while len(queue):
        node, depth = queue.pop(0)
        if stuff_to_print.get(depth):
            stuff_to_print[depth].append(node.value)
        else:
            stuff_to_print.update({depth: [node.value]})
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return stuff_to_print


def serialize(tree):
    stuff_to_print = []
    queue = [tree]
    while len(queue):
        node = queue.pop(0)
        stuff_to_print.append(node.value)
        if node.left:
            queue.append(node.left)
        if not node.left:
            stuff_to_print.append(None)
        if node.right:
            queue.append(node.right)
        if not node.right:
            stuff_to_print.append(None)

    return stuff_to_print


def deserialize(list_of_values):
    tree = BinaryTreeNode(list_of_values[0])
    for value in list_of_values[1:]:
        if value:
            tree = insert(tree, value)

    return tree


