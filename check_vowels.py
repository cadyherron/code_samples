vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def halvesAreAlike(s: str) -> bool:
    mid = len(s) // 2
    left = s[:mid]
    right = s[mid:]
    index = 0
    left_vowels = 0
    right_vowels = 0

    while index < mid:
        left_letter = left[index]
        if left_letter in vowels:
            left_vowels += 1
        right_letter = right[index]
        if right_letter in vowels:
            right_vowels += 1

        index += 1

    return left_vowels == right_vowels
