data1 = [12, 97, 1, 1024, 7,  6, 846, 106]
data2 = [5, 9, 3, 7, 2, 8, 1, 6]

# TO-DO: complete the helper function below to merge 2 sorted arrays

# current plan of attack
# we need to take two sorted arrays and merge them together
# sorting them as we merge them

# check each index


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO

    # first off, figure out what merged_arr is
    print("merged_arr", merged_arr)

    # check whats in arrA and arrB
    print("arrA : ", arrA)
    print("arrB : ", arrB)

    # create index tracker for arrA and arrB
    idxA = 0
    idxB = 0


# for loop isn't really working here, because we need
# the indexes of the arrays. Why don't we switch to
# using a range based on the length of the arrays
# instead of items w/in the arrays
    for i in range(0, len(arrA)):
        print(f"i : {i}")
        print(f"arrA[i] : {arrA[i]}")
        for ib in range(0, len(arrB)):
            # if the value of item in arrA is larger
            # than value of item in arrB, insert it into
            # arrB at the index after the current item in arrB
            # (moving arrB item to the left)
            if arrA[i] > arrB[ib]:
                print("bigger")

            # if the value of item in arrA is smaller
            # than value of item in arrB, insert it into
            # arrB at the index of the current item in arrB
            # (moving arrB item to the right)
            if arrA[i] < arrB[ib]:
                print("smaller")
            print(f"ib : {ib}")
            print(f"arr[ib] : {arrB[ib]}")

    #     print(f"1. merged_arr[i] : {merged_arr[i]}")
    #     merged_arr[i] = 1
    #     print(f"2. merged_arr[i] : {merged_arr[i]}")

    return merged_arr


merge(data1, data2)

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
