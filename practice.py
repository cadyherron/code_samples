def merge_sort(my_list: list):
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]

        merge_sort(left)
        merge_sort(right)

        l = 0
        r = 0
        i = 0
        # we have items left in each list
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                my_list[i] = left[l]
                l += 1
            else:
                my_list[i] = right[r]
                r += 1
            i += 1

        while l < len(left):
            my_list[i] = left[l]
            i += 1
            l += 1

        while r < len(right):
            my_list[i] = right[r]
            i += 1
            r += 1


class BinaryTreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return BinaryTreeNode(value)
    if root.value < value:
        root.right = insert(root.right, value)
    else:
        root.left = insert(root.left, value)

    return root
