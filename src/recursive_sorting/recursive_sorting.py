data1 = [1, 2, 3, 4, 5, 6, 7, 8]
data2 = [100, 101, 102, 103, 104, 105, 106, 107]

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

    return arr


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
