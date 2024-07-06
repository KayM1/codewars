def bubble_sort(arr):
    for i in range(len(arr)):
        j = len(arr) - 1
        while j > i:
            if arr[j] < arr[j-1]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    return arr

array = [20, 32, 5, 3, 2, 4, 1]
print(bubble_sort(array))