data1 = [1, 2, 3, 4, 5, 6, 7, 8]
data2 = [100, 101, 102, 103, 104, 105, 106, 107]
data3 = [37, 42, 67, 1, 9, 3, 10, 4, 12]

# TO-DO: complete the helper function below to merge 2 sorted arrays

# current plan of attack
# we need to take two sorted arrays and merge them together
# sorting them as we merge them

# check each index


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    for i in range(elements):
        print(
            f"i : {i}\n arrA : {arrA}\n arrB : {arrB}\n merged_arr : {merged_arr}\n\n\n")
        # if length of arrA is 0, then move items from
        # beginning of arrB into the merged_arr by swapping
        # the values
        if len(arrA) == 0:
            merged_arr[i] = arrB.pop(0)
        elif len(arrB) == 0:
            merged_arr[i] = arrA.pop(0)
        # check beginning indexes against each other
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA.pop(0)
        else:
            merged_arr[i] = arrB.pop(0)

    return merged_arr


mester1 = merge(data1, data2)
print(mester1)

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # TO-DO
    # we have a helper function that merges sorted arrays
    # we know that an array of len = 1 is sorted
    # therefore, we need to split the array coming in
    # recursively until it is len = 1
    # and then run our merge() helper function

    # 1. while loop that checks if len(arr) > 1
    # 2. if (1) is true, split arr in half to lhs and rhs arrays
    # 3. if len(arr) = 1, then run merge on it (with another sorted array)

    # instantiate lhs and rhs arrays
    lhs = []
    rhs = []

    if len(arr) > 1:
        print(f"arr length = {len(arr)}")
        lhs = merge_sort(merge_sort(arr[: len(arr) // 2]))
        rhs = merge_sort(merge_sort(arr[len(arr) // 2:]))
        arr = merge(lhs, rhs)
        print(f"arr : {arr}")

    return arr


merge_sort_test_1 = merge_sort(data3)

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
