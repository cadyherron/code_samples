"""
Write an efficient function that checks whether any permutation ↴ of an input string is a palindrome.

You can assume the input string only contains lowercase letters.

Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False

"""


# there can be 1 odd letter and the rest should be multiples of 2
# racecar, r: 2, a: 2, c: 2, e: 1
# loop through the string, key is the letter and value is the number of times we've seen it

def is_palindrome(thing):
    inventory = {}
    for letter in thing:
        if inventory.get(letter):
            inventory[letter] += 1
        else:
            inventory[letter] = 1

    has_odd = False
    for count in inventory.values():
        if count % 2 != 0 and has_odd is True:
            return False
        elif count % 2 != 0:
            has_odd = True

    return True


def has_palindrome_permutation(thing):
    unpaired_characters = set()
    for char in thing:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    return len(unpaired_characters) <= 1
