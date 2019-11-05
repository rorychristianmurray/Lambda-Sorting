
# test_arr = [
#     "item1",
#     "item3",
#     "item7",
#     "item5",
#     "item2",
#     "item4",
#     "item6",
# ]

# # TO-DO: Complete the selection_sort() function below


# def sortbox(arr):

#     # for all indices except last index (indicates a for loop)
#     # loop through elements on RHS and cur_index and find smallest element
#     # swap the element at current index with smallest element
#     ## found in loop

#     # in order to do this, we need to do a few things
#     # 1. loop through the list
#     # 2. compare the current index we are on
#     # to the smallest index we have set
#     # if the current index we are on in the loop
#     # is smaller than the smallest_index we have set,
#     # we need to swap the current index and the smallest index

#     # loop through n-1 elements
#     for i in range(0, len(arr) - 1):
#         temp = arr[i]
#         cur_index = i
#         smallest_index = cur_index
#         # TO-DO: find next smallest element
#         # (hint, can do in 3 loc)
#         # we can look at the unsorted array portion, which will be
#         # the part to the right from the current index

#         # 1. run the nested loop from the right of the cur_index to the end of the unsorted array
#         # 2. compare the value at the smallest_idx to the value at
#         # the cur_idx
#         # 3. if the smallest_idx value is larger, swap the indexes

#         for cur_index in range(cur_index+1, len(arr)):
#             if arr[smallest_index] > arr[cur_index]:
#                 smallest_index = cur_index

#         # TO-DO: swap
#         arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

#     return arr


# # print(sortbox(test_arr))


# def boxsort(arr):
#     # loop through each element in the array
#     # for each element, compare it to its neighbor on the right
#     # if the value of the cur element is larger than the value
#     # of the element to the right, swap them
#     # run until no more comparisons
#     print("in boxsort")

#     for i in range(0, len(arr)):
#         # what are we working with?
#         print("i", i)
#         cur_index = i
#         compare_index = i + 1

#         # keep running loop until the value of the
#         # element to the left of the cur element is
#         # larger then the value of the cur element
#         # and we haven't completed a loop
#         while cur_index > 0 and arr[curr_index - 1] > curr_index:
#             # compare - how?
#             # if val of cur element is larger than value to its right then swap them
#             if arr[cur_index] > arr[cur_index + 1]:
#                 arr[i], arr[i + 1] = arr[i + 1], arr[i]

#     # swap - how?

#     return arr

#     # print(boxsort(num_arr))


##########################################

num_arr = [
    1,
    3,
    7,
    5,
    2,
    4,
    6,
]


def testone(arr):

    # we get a count which is the length of the array
    count = len(arr)
    print(f"count: {count}")

    # for every element of the array
    # need to use a while loop to keep it going after
    # the first return

    # while arr[i] < arr[i - 1] or arr[i] > arr[i + 1]:

    while count > 0:
        for i in range(0, len(arr) - 1):
            print("arr[i] : ", arr[i])
            print("arr[i + 1] : ", arr[i + 1])
            print("arr[i - 1] : ", arr[i - 1])
            if arr[i] <= arr[i + 1]:
                count -= 1
                print(f"count: {count}")
            else:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                count = len(arr)

    return arr


print(testone(num_arr))


# def testtwo(arr):
#     # for every element of the array
#     # need to use a while loop to keep it going after
#     # the first return
#     for i in range(0, len(arr) - 1):
#         print("arr[i] : ", arr[i])
#         print("arr[i + 1] : ", arr[i + 1])
#         print("arr[i - 1] : ", arr[i - 1])
#         if arr[i] > arr[i + 1]:
#             arr[i], arr[i + 1] = arr[i + 1], arr[i]

#     return arr


# print(testtwo(num_arr))
