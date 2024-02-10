def pair_with_sum_in_rotated_array(arr, target):
    # Find the pivot point using binary search
    def find_pivot(arr):
        low = 0
        high = len(arr) - 1

        while low < high:
            mid = (low + high) // 2
            if arr[mid] > arr[high]:
                low = mid + 1
            else:
                high = mid

        return low

    # Function to check if a pair with given sum exists
    def pair_exists(arr, target):
        left = 0
        right = len(arr) - 1

        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == target:
                return True
            elif current_sum < target:
                left = (left + 1) % len(arr)  # Move the left pointer
            else:
                right = (right - 1 + len(arr)) % len(arr)  # Move the right pointer

        return False

    pivot = find_pivot(arr)

    # If pivot is 0, then the array is not rotated
    if pivot == 0:
        return pair_exists(arr, target)

    # If pivot is found, then divide the array into two subarrays and check if the pair exists in any of them
    left_subarray = arr[:pivot]
    right_subarray = arr[pivot:]

    return pair_exists(left_subarray, target) or pair_exists(right_subarray, target)

# Example usage:
arr = [11, 15, 26, 38, 9, 10]
target = 35
print(pair_with_sum_in_rotated_array(arr, target))  # Output: True
