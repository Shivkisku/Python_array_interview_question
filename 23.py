def segregate_zeros_and_ones(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Move the left pointer until it encounters a 1
        while arr[left] == 0 and left < right:
            left += 1
        # Move the right pointer until it encounters a 0
        while arr[right] == 1 and left < right:
            right -= 1
        # Swap 0s and 1s
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

# Example usage:
arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
print("Segregated array:", segregate_zeros_and_ones(arr))  # Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
