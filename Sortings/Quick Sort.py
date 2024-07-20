# Quick Sort
"""
This algorithm uses a pointer pivot to point to a value. Aim is to sort the pivot and recursively divide the array and
introduce new pivots and sort them.
"""

"""
Steps - 
1. Introduce the pivot pointer - usually the first element of array. 
2. Use a for loop to start from the 2nd element. Also, use a swap pointer that starts from pivot.
3. Compare the next element to pivot. If its greater than pivot, iterate. If its lesser than pivot, iterate swap by one.
4. Swap both the number lesser than pivot with that of number with swap pointer. Continue the iteration.
5. Once the loop is complete, swap both pivot and swap. The pivot is sorted and new sub-arrays are available. 
6. Repeat the steps from first element till the swap and from swap+1 till the end.
"""


def swap(list1, index1, index2):
    list1[index1], list1[index2] = list1[index2], list1[index1]


def pivot(list1, pivot_index, end_index):
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if list1[i] < list1[pivot_index]:
            swap_index += 1
            swap(list1, swap_index, i)
    swap(list1, pivot_index, swap_index)
    return swap_index

def quickSort_helper(list1, left, right):
    if left < right:
        pivot_index = pivot(list1, left, right)
        quickSort_helper(list1, left, pivot_index)
        quickSort_helper(list1, pivot_index + 1, right)
    return list1

def QuickSort(list1):
    return quickSort_helper(list1, 0, len(list1)-1)

my = [5, 10, 2, 1 ,15, 22, 20]
print(QuickSort(my))



