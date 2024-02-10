def min_swaps(arr, k):
    n = len(arr)
    
    # Count the number of elements less than or equal to k
    count = 0
    for num in arr:
        if num <= k:
            count += 1
    
    # Count the number of elements less than or equal to k in the first window of size count
    window_count = 0
    for i in range(count):
        if arr[i] <= k:
            window_count += 1
    
    min_swaps = count - window_count
    
    # Iterate through the array to find the maximum count of elements less than or equal to k in any window of size count
    for i in range(count, n):
        # Update window count when the window slides
        if arr[i - count] <= k:
            window_count -= 1
        if arr[i] <= k:
            window_count += 1
        min_swaps = min(min_swaps, count - window_count)
    
    return min_swaps

# Example usage:
arr1 = [2, 1, 5, 6, 3]
k1 = 3
print("Minimum number of swaps:", min_swaps(arr1, k1))  # Output: 1

arr2 = [2, 7, 9, 5, 8, 7, 4]
k2 = 5
print("Minimum number of swaps:", min_swaps(arr2, k2))  # Output: 2
