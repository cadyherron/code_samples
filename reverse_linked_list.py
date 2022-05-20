"""
Reverse a linked list in place

One input = the head of the list
One output = new head of the list
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_linked_list(head):
    """
    our head will no longer have a .next and will be the tail
    each node will have its .next be the node that USED to point to itself
    """
    current_node = head
    previous_node = None
    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node

