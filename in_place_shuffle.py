"""
Write a function for doing an in-place shuffle of a list.

The shuffle must be "uniform," meaning each item in the original list must have the same probability of
    ending up in each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.

"""
# [1,2,3,4,5] becomes [3,5,4,2,1]
# we can use the index to randomly assign a new index
# we need to keep track of what we've already used: set()
# how many shuffles do we need to do? go through the whole list? does that make it uniform?


import random


def in_place_shuffle(ints):
    available_indices = set(range(0, len(ints)))
    for index, num in enumerate(ints):
        new_index = random.sample(available_indices, 1)[0]
        ints[index], ints[new_index] = ints[new_index], ints[index]
        available_indices.remove(new_index)

    return ints


