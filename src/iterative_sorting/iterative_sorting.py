# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):

    # for all indices except last index (indicates a for loop)
    # loop through elements on RHS and cur_index and find smallest element
    # swap the element at current index with smallest element
    ## found in loop

    # in order to do this, we need to do a few things
    # 1. loop through the list
    # 2. compare the current index we are on
    # to the smallest index we have set
    # if the current index we are on in the loop
    # is smaller than the smallest_index we have set,
    # we need to swap the current index and the smallest index

    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        temp = arr[i]
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # we can look at the unsorted array portion, which will be
        # the part to the right from the current index

        # 1. run the nested loop from the right of the cur_index to the end of the unsorted array
        # 2. compare the value at the smallest_idx to the value at
        # the cur_idx
        # 3. if the smallest_idx value is larger, swap the indexes

        for cur_index in range(cur_index+1, len(arr)):
            if arr[smallest_index] > arr[cur_index]:
                smallest_index = cur_index

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
