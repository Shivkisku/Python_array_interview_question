def max_length_subarray_with_equal_zeros_and_ones(arr):
    # Initialize variables
    max_length = 0
    sum_index_map = {}
    curr_sum = 0

    # Traverse the array
    for i in range(len(arr)):
        # Update current sum
        if arr[i] == 0:
            curr_sum -= 1
        else:
            curr_sum += 1

        # If current sum is 0, update max_length
        if curr_sum == 0:
            max_length = i + 1

        # If current sum is seen before, update max_length
        if curr_sum in sum_index_map:
            max_length = max(max_length, i - sum_index_map[curr_sum])
        else:
            sum_index_map[curr_sum] = i

    return max_length

# Example usage:
arr = [0, 1, 0, 1, 1, 0, 0]
print("Largest subarray with equal 0s and 1s length:", max_length_subarray_with_equal_zeros_and_ones(arr))  # Output: 6
