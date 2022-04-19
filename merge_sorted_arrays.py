"""
Write a function to merge our lists of orders into one sorted list.

For example:

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))
"""


def merge_lists(my_list, alices_list):
    merged_list_size = len(my_list) + len(alices_list)
    merged_list = [None] * merged_list_size
    current_index_alice = 0
    current_index_mine = 0
    current_index_merged = 0
    while current_index_merged < merged_list_size:
        my_list_exhausted = current_index_mine >= len(my_list)
        alices_list_exhausted = current_index_alice >= len(alices_list)

        if (not my_list_exhausted and
                (alices_list_exhausted or my_list[current_index_mine] < alices_list[current_index_alice])):
            merged_list[current_index_merged] = my_list[current_index_mine]
            current_index_mine += 1
        else:
            merged_list[current_index_merged] = alices_list[current_index_alice]
            current_index_alice += 1

        current_index_merged += 1

    return merged_list

