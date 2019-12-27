def merge_v1(left, right):
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


def merge_sort_v1(array):
    """Merge sort algorithm implementation."""
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort_v1(array[:mid])
    right = merge_sort_v1(array[mid:])
    return merge_v1(left, right)


def merge_v2(a, b):
    """Merge sort merging function."""
    temp_arr = []

    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            temp_arr.append(a[0])
            a.remove(a[0])
        else:
            temp_arr.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        temp_arr += b
    else:
        temp_arr += a
    return temp_arr

def merge_sort_v2(array):
    """Merge sort algorithm implementation."""
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = merge_sort_v2(array[:mid])
    right = merge_sort_v2(array[mid:])
    return merge_v2(left, right)


print("Merge sort (v1): ", merge_sort_v1([8, 6, 9, 3, 1, -5, 7]))
print("Merge sort (v2): ", merge_sort_v2([8, 6, 9, 3, 1, -5, 7]))
