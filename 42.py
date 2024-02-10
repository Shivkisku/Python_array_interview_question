def min_merge_operations_to_palindrome(arr):
    left = 0
    right = len(arr) - 1
    merge_count = 0

    while left < right:
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        elif arr[left] < arr[right]:
            arr[left + 1] += arr[left]
            left += 1
            merge_count += 1
        else:
            arr[right - 1] += arr[right]
            right -= 1
            merge_count += 1

    return merge_count

# Example usage:
arr1 = [15, 4, 15]
print("Minimum merge operations:", min_merge_operations_to_palindrome(arr1))  # Output: 0

arr2 = [1, 4, 5, 1]
print("Minimum merge operations:", min_merge_operations_to_palindrome(arr2))  # Output: 1

arr3 = [11, 14, 15, 99]
print("Minimum merge operations:", min_merge_operations_to_palindrome(arr3))  # Output: 3
