#import numpy as np
# arr = np.random.randint(1, 20, 10)

arr = [2, 5, 9, 8, 2, 8, 7, 10, 4, 3]
# arr = [13, 13, 13, 16, 14, 18, 11, 11, 19, 11]
# arr = [9, 13, 3, 6, 14, 18, 11, 11, 19, 11]
# arr = [18, 16, 17, 4, 9, 7, 7, 14, 11, 14,]
# arr = [12, 3, 3, 20, 5]
print("Initial array:", arr)


def max_min(arr):
    arr_min = arr[0]
    arr_max = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < arr_min:
            arr_min = arr[i]
        if arr[i] > arr_max:
            arr_max = arr[i]
    return (arr_min, arr_max)

# count = [0 for i in range(len(arr))] # won't work!!!!!!!


def counting_sort_method1(array):
    # not stable algorithm
    arr_min, arr_max = max_min(array)
    count = [0 for i in range((arr_max - arr_min) + 1)]
    print(count)
    for i in array:
        count[i - arr_min] += 1
    print(count)

    j = 0
    for i in range(arr_min, arr_max + 1):
        while count[i - arr_min] > 0:
            array[j] = i
            j += 1
            count[i - arr_min] -= 1
    return array


def counting_sort_method2(array):
    # stable algorithm
    arr_min, arr_max = max_min(array)
    # count = [0 for i in range((arr_max - arr_min) + 1)]
    count = [0 for i in range(0, arr_max + 1)]
    print(count)
    for i in array:
        count[i] += 1
    print(count)
    # running sum ([2, 2, 3,...] there are 3 occurrences of values <= 3)
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    print(count)

    b = [None] * len(arr)
    k = len(arr) - 1
    while k >= 0:
        b[count[arr[k]] - 1] = arr[k]
        print(b)
        count[arr[k]] -= 1
        k -= 1
    return b


result1 = counting_sort_method1(arr)
print("Counting sort (v1):", result1)
print("-------------------")
result2 = counting_sort_method2(arr)
print("Counting sort (v2):", result2)
