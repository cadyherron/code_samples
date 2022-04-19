"""
Write a function that takes a list of characters and reverses the letters in place

["h", "e", "l", "l", "o"] becomes ["o", "l", "l", "e", "h"]
["h", "e", "l", "p"] becomes ["p", "l", "e", "h"]

even length: split the array in two and swap from the outside in
odd length: split the array in two around the middle element, then swap from the outside in

"""


# first pass
def reverse_in_place(chars):
    length = len(chars)
    is_odd = length % 2 > 0
    if is_odd:
        middle_index = int((length - 1) / 2)
    else:
        middle_index = int(length / 2) - 1

    left_index = 0
    right_index = length - 1

    while left_index <= middle_index:
        new_right = chars[left_index]
        chars[left_index] = chars[right_index]
        chars[right_index] = new_right
        left_index += 1
        right_index -= 1

    print(chars)


# simplified
def reverse_list(chars):
    left_index = 0
    right_index = len(chars) - 1

    while left_index < right_index:
        chars[left_index], chars[right_index] = chars[right_index], chars[left_index]
        left_index += 1
        right_index -= 1

    print(chars)


if __name__ == "__main__":
    reverse_in_place(["h", "e", "l", "l", "o"])
    reverse_list(["h", "e", "l", "l", "o"])
