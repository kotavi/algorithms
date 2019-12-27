import time
import numpy as np

rand_nums = np.random.randint(-100, 101, 10)
start_time = time.time()


def selection_sort(array):
    threshold = len(array) - 1

    while threshold > 0:
        largest = 0
        for i in range(1, threshold + 1):
            if array[i] > array[largest]:
                largest = i
        if threshold != largest:
            temp = array[largest]
            array[largest] = array[threshold]
            array[threshold] = temp
        threshold -= 1


selection_sort(rand_nums)

print("--- %s seconds ---" % (time.time() - start_time))

for i in range(0, len(rand_nums)):
    print(rand_nums[i])
