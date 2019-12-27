# pycodestyle --first algorithms/InserionSortAlgorithm.py


def insertion_sort_algorithm(array):
    for threshold in range(1, len(array)):
        new_element = array[threshold]
        j = threshold - 1
        while j >= 0 and new_element < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = new_element
    return array


res = insertion_sort_algorithm([1, 4, 21, 1000, 44, 7, 14, 17, -20, 32, -90])
for i in range(0, len(res)):
    print(res[i], end=", ")
