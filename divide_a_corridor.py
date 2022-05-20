"""
corridor is a string of length n where "S" represents a seat and "P" represents a plant

Divide the corridor into non-overlapping sections, where each section has exactly two seats with any number of plants.

Return the number of ways to divide the corridor.

EXAMPLE 1:
    Input: corridor = "SSPPSPS"
    Output: 3
        SS | PPSPS
        SSP | PSPS
        SSPP | SPS


EXAMPLE 2:
    Input: corridor = "PPSPSP"
    Output: 1 --> installing any more dividers would create a section with less than 2 seats


EXAMPLE 3:
    Input: corridor = "SPPSPSPPPS"
    Output: 2
        SPPS | PSPPPS
        SPPSP | SPPPS
"""
# how do we do this by hand? identify the smallest sections with 2 seats, then find permutations around plants
# if we get 3 S in a row, we need to put in a divider
# depth-first search: what are we looking for? start + end index, then unique?
# do we want all the possible sub-arrays and throw out any with S < 2?


def divide_corridor(corridor: str) -> int:
    corr = list(corridor)
    num_seats = corr.count("S")
    if len(corr) < 2 or len(corr) == 2 and corr != ["S", "S"] or num_seats % 2:
        return 0

    if num_seats == 2:
        return 1

    valid_dividers = set()
    for divider in range(2, len(corr)):
        # if left of divider has 2 seats and right of divider has 2 seats, add to valid_dividers
        left_seats = corr[:divider].count("S")
        right_seats = corr[divider:].count("S")
        if left_seats == 2 and right_seats == 2:
            valid_dividers.add(divider)

    return len(valid_dividers)


def number_of_ways(corridor: str) -> int:
    current_count = 0
    a = 0
    answer = 1
    seat_count = corridor.count("S")
    if len(corridor) < 2 or len(corridor) == 2 and corridor != "SS" or seat_count % 2:
        return 0

    if seat_count == 2:
        return 1

    for item in corridor:
        if item == "S":
            seat_count -= 1
            current_count += 1
        if seat_count == 0:
            return answer
        if current_count > 2:
            current_count = 1
            answer *= a
            answer %= (10**9 + 7)
            a = 0
        if current_count == 2:
            a += 1

    return answer


if __name__ == "__main__":
    number_of_ways("SSPPPSSPPP")


# another great solution:
# https://leetcode.com/problems/number-of-ways-to-divide-a-long-corridor/discuss/1745400/Python-O(N)-With-Explanation-**EASIEST-TO-UNDERSTAND**