import time
import numpy as np

rand_nums = np.random.randint(-100, 101, 20)
start_time = time.time()


# Algorithm's complexity - O(n^2)
# In-place algorithm
def bubble_sort_in_descending_order(array):
    threshold = len(array) - 1

    while threshold > 0:
        for i in range(0, threshold):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                # temp = array[i]
                # array[i] = array[i + 1]
                # array[i + 1] = temp
        threshold -= 1
    return array


# rand_nums = [1, 4, 21, 1000, 44, 7, 14, 17, -20, 32]
bubble_sort_in_descending_order(rand_nums)

print("--- %s seconds ---" % (time.time() - start_time))

for i in range(0, len(rand_nums)):
    print(rand_nums[i], end=", ")
