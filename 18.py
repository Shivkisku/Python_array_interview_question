def three_way_partition(arr, low_val, high_val):
    n = len(arr)
    # Initialize pointers for three-way partitioning
    low = 0
    mid = 0
    high = n - 1

    # Traverse the array and partition it
    while mid <= high:
        if arr[mid] < low_val:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif low_val <= arr[mid] <= high_val:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

# Example usage:
arr = [4, 3, 7, 6, 2, 8, 1, 5, 9]
low_val = 3
high_val = 7
result = three_way_partition(arr, low_val, high_val)
print("Partitioned Array:", result)
