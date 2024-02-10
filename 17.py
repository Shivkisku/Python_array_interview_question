def rearrange_alternatively(arr):
    n = len(arr)
    # Count the number of positive and negative numbers
    pos_count = sum(1 for num in arr if num > 0)
    neg_count = n - pos_count

    # Initialize pointers for positive and negative numbers
    pos_idx = 0
    neg_idx = 0

    # If there are more positive numbers, they should appear at the end
    if pos_count >= neg_count:
        while pos_idx < n and neg_idx < n:
            # Find the next positive index
            while pos_idx < n and arr[pos_idx] < 0:
                pos_idx += 1
            # Find the next negative index
            while neg_idx < n and arr[neg_idx] >= 0:
                neg_idx += 1
            # Swap positive and negative numbers
            if pos_idx < n and neg_idx < n:
                arr[pos_idx], arr[neg_idx] = arr[neg_idx], arr[pos_idx]
                pos_idx += 1
                neg_idx += 1
    # If there are more negative numbers, they should appear at the end
    else:
        while pos_idx < n and neg_idx < n:
            # Find the next positive index
            while pos_idx < n and arr[pos_idx] < 0:
                pos_idx += 1
            # Find the next negative index
            while neg_idx < n and arr[neg_idx] >= 0:
                neg_idx += 1
            # Swap positive and negative numbers
            if pos_idx < n and neg_idx < n:
                arr[neg_idx], arr[pos_idx] = arr[pos_idx], arr[neg_idx]
                pos_idx += 1
                neg_idx += 1

    return arr

# Example usage:
arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
result = rearrange_alternatively(arr)
print("Rearranged Array:", result)
