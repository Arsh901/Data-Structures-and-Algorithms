# Selection Sort
"""We repeatedly find the minimum element and move it to sorted part of array to make unsorted part sorted"""

"""
When to use this sorting -
  --> When size of the list is small. 
  --> No extra space is needed i.e. we have insufficient space
When to avoid - 
  --> The size of list is very large. Finding min element again and again is difficult
  --> Huge time complexity
"""

def selection_sort(customList):
    for i in range(len(customList)):
        min_index = i
        for j in range(i+1, len(customList)):
            if customList[min_index]>customList[j]:
                min_index = j
        customList[i], customList[min_index] = customList[min_index], customList[i]
    print(customList)

selection_sort([9, 11, 4, 20, 15, 1, 22, 14])

# Time Complexity - O(N) and Space Complexity - O(1)





