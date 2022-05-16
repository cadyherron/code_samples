"""
Check if a singly-linked list has a cycle

Cycle means a node's .next points back to a previous node in the list
"""


class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


head = LinkedListNode(1)
two = LinkedListNode(2)
head.next = two
three = LinkedListNode(3)
two.next = three
four = LinkedListNode(4)
four.next = head


def contains_cycle(linked_list):
    nodes_seen = []
    stack = [linked_list]
    while len(stack):
        node = stack.pop()
        if node.next and node.next in nodes_seen:
            return True
        if node.next:
            stack.append(node)


def contains_cycle_two_runners(first_node):
    slow_runner = first_node
    fast_runner = first_node
    while fast_runner is not None and fast_runner.next is not None:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next
        if fast_runner is slow_runner:  # is: a test if two variables refer to the same object
            return True

    return False

