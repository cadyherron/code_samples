"""
Given an integer array nums and an integer k, return the number of non-empty sub-arrays that have a sum divisible by k.

A subarray is a contiguous part of an array.

Example 1:
Input:          nums = [4,5,0,-2,-3,1], k = 5
Output:         7
Explanation:    There are 7 sub-arrays with a sum divisible by k = 5:
                [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]


Example 2:
Input:          nums = [5], k = 9
Output:         0
"""
# part 1: find all the sub-arrays? and while we're finding the sub-arrays we can evaluate the sum?
# there's a left index and a right index
# 0 1 2 3 4 5
# 5 4 3 2 1 0
# how can we do better than n!


from typing import List


def sub_arrays(nums: List[int], k: int):
    if k == 0:
        return 0

    output = 0
    for left in range(0, len(nums) + 1):
        for right in range(left + 1, len(nums) + 1):
            if left == right:
                continue
            print(f"left and right: {left}, {right}")
            print(f"{nums[left:right]}")
            if sum(nums[left:right]) % k == 0:
                output += 1

    return output


sub_arrays([4, 5, 0, -2, -3, 1], 5)
sub_arrays([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 5)
