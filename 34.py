def smallest_non_sum(arr):
    max_sum = 1

    for num in arr:
        if num <= max_sum:
            max_sum += num
        else:
            break

    return max_sum

# Example usage:
arr1 = [1, 10, 3, 11, 6, 15]
print("Smallest non-sum:", smallest_non_sum(arr1))  # Output: 2

arr2 = [1, 1, 1, 1]
print("Smallest non-sum:", smallest_non_sum(arr2))  # Output: 5

arr3 = [1, 1, 3, 4]
print("Smallest non-sum:", smallest_non_sum(arr3))  # Output: 10

arr4 = [1, 2, 5, 10, 20, 40]
print("Smallest non-sum:", smallest_non_sum(arr4))  # Output: 4

arr5 = [1, 2, 3, 4, 5, 6]
print("Smallest non-sum:", smallest_non_sum(arr5))  # Output: 22
