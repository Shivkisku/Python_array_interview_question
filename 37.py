def max_index_difference(arr):
    n = len(arr)

    # Initialize left_min array
    left_min = [0] * n
    left_min[0] = arr[0]
    for i in range(1, n):
        left_min[i] = min(left_min[i - 1], arr[i])

    # Initialize right_max array
    right_max = [0] * n
    right_max[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], arr[i])

    # Initialize pointers
    i = 0
    j = 0
    max_diff = 0

    # Traverse the array and update max_diff
    while i < n and j < n:
        if left_min[i] <= right_max[j]:
            max_diff = max(max_diff, j - i)
            j += 1
        else:
            i += 1

    return max_diff

# Example usage:
arr1 = [34, 8, 10, 3, 2, 80, 30, 33, 1]
print("Maximum index difference:", max_index_difference(arr1))  # Output: 6

arr2 = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
print("Maximum index difference:", max_index_difference(arr2))  # Output: 8
