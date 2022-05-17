"""
One way to serialize a binary tree is to use preorder traversal.

Given a string of comma-separated values preorder, return true if it is a correct preorder traversal
    serialization of a binary tree.

            9
         3    2
      4   1  #   6
    # #  # #     # #

Example 1:
    Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    Output: true


Example 2:
    Input: preorder = "1,#"
    Output: false


Example 3:
    Input: preorder = "9,#,#,1"
    Output: false
"""
# this is a depth-first traversal, so we'll use a stack


def is_valid_serialization(preorder: str) -> bool:
    stack = []
    for node in preorder.split(","):
        stack.append(node)
        while len(stack) > 2 and stack[-1] == "#" and stack[-2] == "#":
            stack.pop()
            stack.pop()
            if stack.pop() == "#":
                return False
            stack.append("#")

        return len(stack) == 1 and stack[-1] == "#"
