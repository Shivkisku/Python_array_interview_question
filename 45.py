def rearrange_alternately(arr):
    n = len(arr)
    result = [0] * n
    left, right = 0, n - 1

    for i in range(n):
        if i % 2 == 0:
            result[i] = arr[right]
            right -= 1
        else:
            result[i] = arr[left]
            left += 1

    return result

# Example usage:
arr1 = [1, 2, 3, 4, 5, 6, 7]
print("Output:", rearrange_alternately(arr1))  # Output: [7, 1, 6, 2, 5, 3, 4]

arr2 = [1, 2, 3, 4, 5, 6]
print("Output:", rearrange_alternately(arr2))  # Output: [6, 1, 5, 2, 4, 3]
