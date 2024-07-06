def insertion_sort_rev(arr):
    for i in range(len(arr)-1, -1, -1):
        key = arr[i]
        
        j = i + 1
        while j < len(arr) and key < arr[j]:
            arr[j - 1] = arr[j]
            j += 1
        arr[j - 1] = key
    return arr
        

array = [12, 500, 0, 2, 4, 9, 8, 3, 20, 100, 21, 1337]
insertion_sort_rev(array)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

array = [12, 500, 0, 2, 4, 9, 8, 3, 20, 100, 21, 1337]
print(insertion_sort(array))

# i ===>
# j <---