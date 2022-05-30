from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.memo = {1: [TreeNode(0)]}

    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n % 2 == 0:
            return []

        if n in self.memo:
            return self.memo[n]

        else:
            tree = []
            for left_subtree_nodes in range(1, n, 2):
                left_sub_trees = self.allPossibleFBT(left_subtree_nodes)
                right_sub_trees = self.allPossibleFBT((n - 1) - left_subtree_nodes)
                for left_sub in left_sub_trees:
                    for right_sub in right_sub_trees:
                        root = TreeNode(0)
                        root.left = left_sub
                        root.right = right_sub
                        tree.append(root)
            self.memo[n] = tree
            return tree


"""
[0]
must have children [0,0]
[0, 0]
can have [null, null, 0, 0] or [0, 0, 0, 0] or [0, 0, null, null]
"""


def twoSum(nums: List[int], target: int) -> List[int]:
    for index, num in enumerate(nums):
        for next_index, next_element in enumerate(nums[index + 1:], start=index + 1):
            if num + next_element == target:
                return [index, next_index]


def two_sum_efficient(nums: List[int], target: int) -> List[int]:
    memo = {}
    for i in range(len(nums)):
        if nums[i] in memo:
            return [memo[nums[i]], i]
        else:
            memo[target - nums[i]] = i
