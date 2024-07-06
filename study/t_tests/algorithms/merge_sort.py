# complexity n log n
# merging left and right will always only have n elements where n = len(arr)
# splitting the array will have a complexity of log n , because the maximum height of a binary tree is 2^h = n elements, thus h = log n

import random

def merge_sort(arr):
    
    # base case: single element or empty list
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    idx_left = 0
    idx_right = 0

    result = []

    while idx_left < len(left) and idx_right < len(right):
        if left[idx_left] < right[idx_right]:
            result.append(left[idx_left])
            idx_left += 1
        else:
            result.append(right[idx_right])
            idx_right += 1
    
    # append the remaining elements from both lists
    result.extend(left[idx_left:])
    result.extend(right[idx_right:])

    return result

array = [random.randrange(1, 20) for _ in range(100)]
print(merge_sort(array))