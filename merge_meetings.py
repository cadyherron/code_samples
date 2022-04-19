"""
Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges

For example, given:
  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:
  [(0, 1), (3, 8), (9, 12)]


- order is not guaranteed
- as we go through the list: what's the smallest start? is this start smaller than another end?
- how do we know if meetings overlap? if second_start < first_end: we keep first_start and second_end
- what if they start and end at the same time? if second_start == first_end: we keep first_start and second_end
- what if the second meeting ends before the first meeting ends?
    - if second_start < first_end AND second_end < first_end: we keep first_start and first_end

all together:
if first_end >= second_start: keep first_start and the LATER end
else: leave them separate

going through the list twice is O(n^2)
if we sort the list first, we can get O(nlogn)

"""


def merge_ranges(meetings):
    meetings = sorted(meetings)
    results = []
    for index, meeting in enumerate(meetings):
        if index == len(meetings) - 1:
            break
        if meeting[1] >= meetings[index+1][0]:
            results.append((meeting[0], max(meeting[1], meetings[index+1][1])))
        else:
            results.append(meeting)

    return results


r = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
