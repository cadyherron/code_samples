"""
Given an array nums of n integers, return an array of all the unique quadruplets
    [nums[a], nums[b], nums[c], nums[d]] such that:

    1. 0 <= a, b, c, d < n
    2. a, b, c, and d are distinct.
    3. nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.

Example 1:
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


Example 2:
    Input: nums = [2,2,2,2,2], target = 8
    Output: [[2,2,2,2]]
"""
# how can we find all the quadruplet permutations?


def find_permutations(nums):
    if len(nums) == 0:
        return []
    if len(nums) == 1:
        return [nums]

    permutations = []
    for i in range(len(nums)):
        this_num = nums[i]
        remaining_nums = nums[:i] + nums[i+1:]
        for permutation in find_permutations(remaining_nums):
            new = [this_num] + permutation
            permutations.append(new)

    return permutations


def unique_quadruplets(nums, target):
    result = []
    permutations = find_permutations(nums)
    for p in permutations:
        quadruplet = sorted(p[0:4])
        if sum(quadruplet) == target and quadruplet not in result:
            result.append(quadruplet)
    return result


if __name__ == "__main__":
    find_permutations([1, 0, -1, 0, -2, 2])
