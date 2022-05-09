"""
I have an alphabetically ordered list that has been "rotated." For example:

  words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

Write a function for finding the index of the "rotation point," which is where I started working
    from the beginning of the dictionary. This list is huge (there are lots of words I don't know)
    so we want to be efficient here.
"""
# everything before the "rotation point" should be in alphabetical order
# aka the first letter of the first word is earlier in the alphabet than the first letter of the last word
# let's split the list in half each time


def rotation_point(words):
    floor_index = 0
    ceiling_index = len(words) - 1
    while floor_index < ceiling_index:
        guess_index = floor_index + ((ceiling_index - floor_index) // 2)

        if words[guess_index] >= words[0]:
            floor_index = guess_index
        else:
            ceiling_index = guess_index

        if floor_index == ceiling_index:
            return ceiling_index
