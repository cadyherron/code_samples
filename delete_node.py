"""
Delete a node from a singly-linked list, given only a variable pointing to that node.
"""


class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c


def delete_node(node):
    """
    We copy c's .next and .value into this node and let the garbage collector pick up the original c
    """
    next_node = node.next
    if next_node:
        node.value = next_node.value
        node.next = next_node.next


delete_node(b)
