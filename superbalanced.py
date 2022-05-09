"""
Write a function to see if a binary tree is "superbalanced"

A tree is "superbalanced" if the difference between the depths of any two leaf nodes is no greater than one.

"superbalanced":
 o
| \
o  o
|\  |\
o o  o o
|
o

not "superbalanced":
 o
| \
o  o
|\
o o
|
o

"""


class BinaryTreeNode(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right


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


def build_tree():
    tree = BinaryTreeNode(50)
    tree = insert(tree, 17)
    tree = insert(tree, 72)
    tree = insert(tree, 12)
    tree = insert(tree, 23)
    tree = insert(tree, 54)
    tree = insert(tree, 76)
    tree = insert(tree, 9)
    tree = insert(tree, 14)
    tree = insert(tree, 19)
    tree = insert(tree, 67)
    return tree


# binary tree but NOT a binary search tree
# do we need to visit every node?
# if we go depth-first, we can exit if we find a leaf with depth +/- 2 from our shallowest and deepest nodes
# depth-first: LIFO stack, append and pop
# if a node has no left and no right, it's a leaf


def is_superbalanced(root):
    if root is None:
        return True

    current_depth = 0
    shallowest = float("-inf")
    deepest = float("inf")
    stack = [(root, shallowest, deepest)]
    while len(stack):
        node, shallowest, deepest = stack.pop()
        if node.left or node.right:
            # we're not at the deepest leaf yet
            if node.left:
                stack.append((node.left, shallowest, current_depth + 1))
            if node.right:
                stack.append((node.right, shallowest, current_depth + 1))
        else:
            # we found a leaf!
            shallowest = current_depth

    return abs(shallowest - deepest) > 2


def is_balanced(root):
    if root is None:
        return True

    depths = []
    stack = [(root, 0)]
    while len(stack):
        node, depth = stack.pop()
        if (not node.left) and (not node.right):
            # we found a leaf!
            if depth not in depths:
                depths.append(depth)
                # we can't have: more than 2 depths, or 2 depths farther than 1 apart
                if (len(depths) > 2) or (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                    return False
        else:
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

    return True
