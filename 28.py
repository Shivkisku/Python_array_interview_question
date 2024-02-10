def max_difference(arr):
    if not arr or len(arr) < 2:
        return -1
    
    min_element = arr[0]
    max_diff = arr[1] - arr[0]
    
    for i in range(1, len(arr)):
        # Update the minimum element encountered so far
        if arr[i] < min_element:
            min_element = arr[i]
        # Update the maximum difference found so far
        elif arr[i] - min_element > max_diff:
            max_diff = arr[i] - min_element
    
    return max_diff

# Example usage:
arr1 = [2, 3, 10, 6, 4, 8, 1]
print("Maximum difference:", max_difference(arr1))  # Output: 8

arr2 = [7, 9, 5, 6, 3, 2]
print("Maximum difference:", max_difference(arr2))  # Output: 2
