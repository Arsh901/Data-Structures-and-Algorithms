# Merge Sort
"""
--> Merge sort is a divide and conquer algorithm
--> Divides the input array in two halves; and we keep recursively until they are too small to break
--> Merge halves by sorting them
"""


def initialize(arr):
    n = len(arr)
    low = 0
    high = n - 1
    mergeSort(arr, low, high)
    return arr


# This function will divide the array until no more division is possible
def mergeSort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergeSort(arr, low, mid)
    mergeSort(arr, mid + 1, high)
    merge(arr, low, high, mid)


# This function uses 2 pointer - left and right to check which element is greater among the two arrays to be merged.
def merge(arr, low, high, mid):
    left = low
    right = mid + 1

    l = []
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            l.append(arr[left])
            left += 1
        else:
            l.append(arr[right])
            right += 1

    # While loops to check which array has remaining elements. Those elements will be directly added to l.
    while left <= mid:
        l.append(arr[left])
        left += 1

    while right <= high:
        l.append(arr[right])
        right += 1

    # Modifying the arr to its merged and sorted form.
    for i in range(len(l)):
        arr[i + low] = l[i]


print(initialize([3, 1, 11, 4, 7, 5, 21, 33, 12, 9]))



