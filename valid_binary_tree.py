"""
Write a function to check that a binary tree is a valid binary search tree.
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


# valid binary search tree:
# nodes to the left are SMALLER than the current node
# nodes to the right are LARGER than the current node

# these are also valid:
    # node only has a left value
    # node only has a right value
    # node has no children

# we can exit:
    # if left is LARGER than the current node
    # if right is SMALLER than the current node


def valid_node(self):
    if self.left and self.left.value > self.value:
        return False
    if self.right and self.right.value < self.value:
        return False
    return True


def insert(root, value):
    if root is None:
        return BinaryTreeNode(value)
    else:
        if root.value == value:
            return root
        elif root.value < value:
            root.right = insert(root.right, value)
        else:
            root.left = insert(root.left, value)
    return root


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


def is_binary_search_tree(root):
    node_and_bounds_stack = [(root, -float("inf"), float("inf"))]  # can also use sys.maxsize
    # depth-first traversal
    while len(node_and_bounds_stack):
        node, lower_bound, upper_bound = node_and_bounds_stack.pop()
        if (node.value <= lower_bound) or (node.value >= upper_bound):
            return False
        if node.left:
            # add the node to our stack, same lower_bound, new upper_bound
            node_and_bounds_stack.append((node.left, lower_bound, node.value))
        if node.right:
            # add the node to our stack, new lower_bound, same upper_bound
            node_and_bounds_stack.append((node.right, node.value, upper_bound))

    return True

# we're evaluating each node against the collective lower_bound and upper_bound
# the tuple is like a snapshot in time


if __name__ == "__main__":
    root = build_tree()
    # print(tree)

