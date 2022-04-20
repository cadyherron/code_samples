"""
You want to build a word cloud, an infographic where the size of a word corresponds to how often it
    appears in the body of text.

To do this, you'll need data. Write code that takes a long string and builds its word cloud data in a dictionary,
    where the keys are words and the values are the number of times the words occurred.

Make reasonable (not necessarily perfect) decisions about capitalized words.
"""
import re


def word_cloud(long_string):
    words = long_string.split(" ")
    # let's assume the first word is capitalized but not a proper noun
    result = {words[0].lower(): 1}
    for word in words[1:]:
        # let's remove punctuation
        word = re.sub(r'[^a-zA-Z\d\s]', '', word)
        if result.get(word):
            result[word] += 1
        else:
            result.update({word: 1})
    return result


def split_words(input_string):
    words = []
    current_word_start_index = 0
    current_word_length = 0
    for i, char in enumerate(input_string):
        if char.isalpha():
            if current_word_length == 0:
                current_word_start_index = i
            current_word_length += 1
        elif not char.isalpha() or i == len(input_string) - 1:
            word = input_string[current_word_start_index:current_word_start_index + current_word_length]
            words.append(word)
            current_word_length = 0

    return words
