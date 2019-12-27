def merge(left, right):
    """Merge sort merging function."""
    left_ind, right_ind = 0, 0
    result = []

    while left_ind < len(left) and right_ind < len(right):
        if left[left_ind] < right[right_ind]:
            result.append(left[left_ind])
            left_ind += 1
        else:
            result.append(right[right_ind])
            right_ind += 1
    result += left[left_ind:]
    result += right[right_ind:]

    return result


def merge_sort(array):
    """Merge sort algorithm implementation."""
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


merge_sort([8, 6, 9, 3, 1, -5, 7])
