"""
Write a recursive function for generating all permutations of an input string. Return them as a set.
"""
# what's the end case? when the length of the set is equal to the number of characters in the string factorial
# "ABC" --> "ABC", "BAC", "BCA", "CAB", "CBA"
# 3! = 3 * 2 * 1 = 6


from math import factorial


def recursive_permutations(input_string, step=0, result=None):
    if result is None:
        result = set()
    if len(result) == factorial(len(input_string)):
        return result
    if step == len(input_string):
        result.add("".join(input_string))
    for i in range(step, len(input_string)):
        input_string_copy = [char for char in input_string]
        input_string_copy[step], input_string_copy[i] = input_string_copy[i], input_string_copy[step]
        recursive_permutations(input_string_copy, step + 1, result)


def get_permutations(string):
    if len(string) <= 1:
        return {string}

    all_chars_except_last = string[:-1]
    last_char = string[-1]
    permutations_without_last = get_permutations(all_chars_except_last)

    permutations = set()
    for permutation in permutations_without_last:
        for position in range(len(all_chars_except_last) + 1):
            new = permutation[:position] + last_char + permutation[position:]
            permutations.add(new)

    return permutations
