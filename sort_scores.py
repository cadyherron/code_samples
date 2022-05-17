"""
Write a function that takes:
    1. a list of unsorted_scores
    2. the highest_possible_score in the game

and returns a sorted list of scores in less than O(nlgn) time

EXAMPLE:

unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

# Returns [91, 89, 65, 53, 41, 37]
sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
"""
# how does the highest_possible_score help us?


from typing import List


def sort_scores(unsorted_scores: List[int], highest_possible_score: int):
    score_counts = [0] * (highest_possible_score + 1)
    for score in unsorted_scores:
        score_counts[score] += 1

    sorted_scores = []
    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]
        for time in range(count):
            sorted_scores.append(score)

    return sorted_scores
