def insertion_sort(array: list):
    for unsorted_index in range(1, len(array)):
        compare_key = array[unsorted_index]
        sorted_index = unsorted_index - 1
        while sorted_index >= 0 and array[sorted_index] > compare_key:
            array[sorted_index + 1] = array[sorted_index]
            sorted_index -= 1
        array[sorted_index + 1] = compare_key

array = [10,13,29,23,80,30,61,53,92,94]
insertion_sort(array)
print(array)