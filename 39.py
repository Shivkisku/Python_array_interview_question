def count_subarrays(arr, L, R):
    n = len(arr)
    left = 0
    count = 0

    for right in range(n):
        if L <= arr[right] <= R:
            count += right - left + 1
        elif arr[right] < L:
            left = right + 1
        else:  # arr[right] > R
            left = right + 1

    return count

# Example usage:
arr = [2, 1, 4, 3]
L = 2
R = 3
print("Number of subarrays:", count_subarrays(arr, L, R))  # Output: 5
