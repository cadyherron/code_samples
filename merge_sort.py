def merge_sort(input_array):
    if len(input_array) > 1:
        mid = len(input_array) // 2
        left = input_array[:mid]
        right = input_array[mid:]

        merge_sort(left)
        merge_sort(right)

        l = 0
        r = 0
        i = 0

        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                input_array[i] = left[l]
                l += 1
            else:
                input_array[i] = right[r]
                r += 1
            i += 1

        while l < len(left):
            input_array[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            input_array[i] = right[r]
            r += 1
            i += 1
