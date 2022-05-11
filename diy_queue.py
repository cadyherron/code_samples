"""
Implement a queue with 2 stacks.
Your queue should have an enqueue and a dequeue method and it should be "first in first out" (FIFO).

Optimize for the time cost of m calls on your queue. These can be any mix of enqueue and dequeue calls.

Assume you already have a stack implementation and it gives O(1) time push and pop.
"""


# what is a queue? a list where we can add an item to the back and access an item from the front
# what is a stack? a list where we can add an item to the back and access an item from the back
#   stack is LIFO: last in, first out

# what if we keep 1 stack in order, and reverse 1 stack?
# [1,2,3,4]
# [4,3,2,1]
# add 5:
# [1,2,3,4,5]
# [5,4,3,2,1]


class MyQueue(object):
    def __init__(self, items):
        self.stack_one = items
        self.stack_two = [r for r in reversed(items)]

    def enqueue(self, item):
        self.stack_one.append(item)
        self.stack_two.insert(0, item)

    def dequeue(self):
        self.stack_two.pop(0)
        return self.stack_one.pop()


class QueueTwoStacks(object):
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if len(self.out_stack) == 0:

            # Move items from in_stack to out_stack, reversing order
            while len(self.in_stack) > 0:
                newest_in_stack_item = self.in_stack.pop()
                self.out_stack.append(newest_in_stack_item)

            # If out_stack is still empty, raise an error
            if len(self.out_stack) == 0:
                raise IndexError("Can't dequeue from empty queue!")

        return self.out_stack.pop()
