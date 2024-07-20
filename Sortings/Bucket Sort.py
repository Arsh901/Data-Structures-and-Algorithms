# Bucket Sort
"""
--> Requires math module to perform certain calculations like sqrt or ceil
--> Create buckets and distributes elements of array into buckets
--> Sort buckets individually
--> Merge buckets after sorting
"""

"""
Step 1 - No. of buckets = round(Sqrt(number of elements))
Step 2 - Appropriate bucket = ceil(Value * number of buckets / maxValue) here ceil rounds a no. up to nearest integer
Step 3 - Sort all buckets using any sorting algorithms
Step 4 - Merge all buckets
"""
import math
def bucket_sort(list1):
   no_of_buckets = round(math.sqrt(len(list1)))
   maxValue = max(list1)
   arr = []
   for i in range(no_of_buckets):
      arr.append([])

   for i in list1:
      index = math.ceil(i*no_of_buckets/maxValue) # This index will always be in range of 1 to number of buckets
      arr[index-1].append(i)

   for i in arr:
      for j in range(len(i)-1):
         for k in range(len(i)-j-1):
            if i[k] > i[k+1]:
               i[k], i[k+1] = i[k+1], i[k]

   l = []
   for i in arr:
      l += i
   print(l)


bucket_sort([2,1,10,14,11,4,7,3])

# Space Complexity - O(N) as arr is being created
# Avoid bucket sort when space is a concern and if negative numbers are present










