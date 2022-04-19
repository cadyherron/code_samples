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
    sorted_meetings = sorted(meetings)
    results = [meetings[0]]
    for this_start, this_end in sorted_meetings[1:]:
        previous_start, previous_end = results[-1]
        if previous_end >= this_start:
            results[-1] = (previous_start, max(previous_end, this_end))
        else:
            results.append((this_start, this_end))

    return results


r = merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
