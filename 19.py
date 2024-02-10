def bitonic_subarray_length(arr):
    n = len(arr)

    # Initialize arrays to store increasing and decreasing lengths at each index
    inc_lengths = [1] * n
    dec_lengths = [1] * n

    # Calculate increasing lengths from left to right
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            inc_lengths[i] = inc_lengths[i - 1] + 1

    # Calculate decreasing lengths from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            dec_lengths[i] = dec_lengths[i + 1] + 1

    # Find the maximum bitonic subarray length
    max_length = 1
    for i in range(n):
        max_length = max(max_length, inc_lengths[i] + dec_lengths[i] - 1)

    return max_length

# Example usage:
arr1 = [12, 4, 78, 90, 45, 23]
arr2 = [20, 4, 1, 2, 3, 4, 2, 10]
arr3 = [10]
arr4 = [10, 20, 30, 40]
arr5 = [40, 30, 20, 10]

print("Bitonic subarray length (Example 1):", bitonic_subarray_length(arr1))  # Output: 5
print("Bitonic subarray length (Example 2):", bitonic_subarray_length(arr2))  # Output: 5
print("Bitonic subarray length (Extreme Example 1):", bitonic_subarray_length(arr3))  # Output: 1
print("Bitonic subarray length (Extreme Example 2):", bitonic_subarray_length(arr4))  # Output: 4
print("Bitonic subarray length (Extreme Example 3):", bitonic_subarray_length(arr5))  # Output: 4
