# Bubble Sort - Also called sinking sort

"""We compare each pair of two adjacent elements and swap them if they are in wrong order
       It takes many rounds to finally sort the entire array"""

"""
When to use bubble sort?
   --> When input is already sorted 
   --> Space is a concern
   --> Easy to implement

When to avoid ?
   --> Avg time complexity is poor
"""
def bubble_sort(customList):
    for i in range(len(customList)-1):
        for j in range(len(customList)-i-1):
            """-i-1 as we compare adjacent pair. So everytime need to decrease the no. of loop."""
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]  # Swapping
    print(customList)

bubble_sort([3, 10, 1, 7, 8, 20, 11])

# Time Complexity - O(N^2) and Space Complexity - O(1)








