"""
Write a function reverse_words() that takes a message as a list of characters
    and reverses the order of the words in place

When writing your function, assume the message contains only letters and spaces, and all words are separated by 1 space.

For example:

message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
print(''.join(message))
"""

# each space determines a "word"
# should we track the indices maybe?


def reverse_list(chars):
    left_index = 0
    right_index = len(chars) - 1

    while left_index < right_index:
        chars[left_index], chars[right_index] = chars[right_index], chars[left_index]
        left_index += 1
        right_index -= 1


def reverse_words(message):
    reverse_list(message)
    words = []
    start = 0
    for index, r in enumerate(message):
        if r == " ":
            words.append((start, index - 1))
            start = index + 1
        if index == len(message) - 1:
            words.append((start, len(message) - 1))

    for start, end in words:
        while start < end:
            message[start], message[end] = message[end], message[start]
            start += 1
            end -= 1
