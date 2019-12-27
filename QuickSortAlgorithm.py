import numpy as np

rand_nums = np.random.randint(-100, 101, 10)


def quick_sort(array, start, end):
    if start < end:
        pi = partition(array, start, end)
        quick_sort(array, start, pi - 1)
        quick_sort(array, pi + 1, end)
    return array


def partition(array, start, end):
    i = start - 1
    pivot = array[end]
    for j in range(start, end):
        if array[j] <= pivot:
            i += 1
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    temp = array[i+1]
    array[i+1] = array[end]
    array[end] = temp
    return i + 1


"""
Another version of Quick Sort
"""


def q_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x >= pivot]
        right = [x for x in arr[1:] if x < pivot]
        return q_sort(right) + [pivot] + q_sort(left)


print("Initial array:", rand_nums)
print("Sorted array (v1):", quick_sort(rand_nums, 0, len(rand_nums) - 1))
print("Sorted array (v2):", q_sort(rand_nums))
