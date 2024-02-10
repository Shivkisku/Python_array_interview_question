def max_subarray_sum(arr, k):
    n = len(arr)
    
    # Calculate the sum of the first k elements
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Iterate through the array and update the window sum
    for i in range(k, n):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    
    return max_sum

# Example usage:
arr1 = [-4, -2, 1, -3]
k1 = 2
print("Maximum subarray sum:", max_subarray_sum(arr1, k1))  # Output: -1

arr2 = [1, 1, 1, 1, 1, 1]
k2 = 2
print("Maximum subarray sum:", max_subarray_sum(arr2, k2))  # Output: 6
