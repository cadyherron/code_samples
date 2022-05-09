"""
"Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

Write a function that, given a sentence like the one above, along with the position of an opening parenthesis,
    finds the corresponding closing parenthesis.

Example: if the example string above is input with the number 10 (position of the first parenthesis),
    the output should be 79 (position of the last parenthesis).


"""


def matching(input_string, opener_index):
    openers = 0
    for position in range(opener_index + 1, len(input_string)):
        char = input_string[position]
        if char == "(":
            openers += 1
        elif char == ")":
            if openers == 0:
                return position
            else:
                openers -= 1

    raise ValueError("No matching closing parenthesis.")






def parenthesis_matching(input_string, open_index):
    # if we see a paren BEFORE opening_index, we need to see a paren AFTER our target
    # we need to see x number of ) before we get to the one we want
    openers = []
    closers = []
    for index, char in enumerate(input_string):
        if char == "(":
            openers.append(index)
        elif char == ")":
            closers.append(index)

    if len(openers) != len(closers):
        raise ValueError("Parens don't match, invalid input")

    print(f"openers: {openers}")
    print(f"closers: {closers}")
    closer_index = openers.index(open_index)
    return closers[closer_index]


