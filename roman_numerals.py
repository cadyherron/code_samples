from typing import List


def roman_numerals(s: str) -> int:
    total = 0
    lookup = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000
    }
    i = 0
    while i < len(s):
        this_letter = s[i]
        look_ahead = s[i:i+2]
        if look_ahead in lookup.keys():
            total += lookup[look_ahead]
            i += 2
        else:
            total += lookup[this_letter]
            i += 1

    return total


def longest_common_prefix(strs: List[str]) -> str:
    prefix = ""
    for i in range(len(strs[0]) - 1):
        match = True
        letter = strs[0][i]
        for word in strs:
            if word[i] != letter:
                return prefix
        prefix += letter

    return prefix

