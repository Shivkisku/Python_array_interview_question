def max_product_subarray(arr):
    if not arr:
        return 0
    
    n = len(arr)
    max_prod = arr[0]
    min_prod = arr[0]
    max_global = arr[0]

    for i in range(1, n):
        # Keep track of maximum and minimum products ending at the current index
        temp_max = max_prod
        max_prod = max(arr[i], max(arr[i] * temp_max, arr[i] * min_prod))
        min_prod = min(arr[i], min(arr[i] * temp_max, arr[i] * min_prod))

        # Update the maximum product found so far
        max_global = max(max_global, max_prod)

    return max_global

# Example usage:
arr = [2, 3, -2, 4]
print("Maximum product subarray:", max_product_subarray(arr))  # Output: 6 (the subarray [2, 3])
