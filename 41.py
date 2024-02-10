def longest_subarray_sum_divisible_by_k(arr, k):
    n = len(arr)
    max_length = 0
    cumulative_sum_mod_k = {0: -1}  # Initialize with a cumulative sum of 0 and index -1

    cumulative_sum = 0
    for i in range(n):
        cumulative_sum += arr[i]
        remainder = cumulative_sum % k

        if remainder in cumulative_sum_mod_k:
            max_length = max(max_length, i - cumulative_sum_mod_k[remainder])
        else:
            cumulative_sum_mod_k[remainder] = i

    return max_length

# Example usage:
arr1 = [2, 7, 6, 1, 4, 5]
k1 = 3
print("Longest subarray length:", longest_subarray_sum_divisible_by_k(arr1, k1))  # Output: 4

arr2 = [-2, 2, -5, 12, -11, -1, 7]
k2 = 3
print("Longest subarray length:", longest_subarray_sum_divisible_by_k(arr2, k2))  # Output: 5
