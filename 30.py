def push_zeros_to_end(arr):
    # Initialize a pointer to keep track of the position to place the non-zero elements
    non_zero_index = 0
    
    # Iterate through the array
    for i in range(len(arr)):
        # If the current element is non-zero, place it at the non_zero_index position
        if arr[i] != 0:
            arr[non_zero_index] = arr[i]
            non_zero_index += 1
    
    # Fill the remaining positions with zeros
    while non_zero_index < len(arr):
        arr[non_zero_index] = 0
        non_zero_index += 1

# Example usage:
arr1 = [1, 2, 0, 4, 3, 0, 5, 0]
push_zeros_to_end(arr1)
print("Modified array:", arr1)  # Output: [1, 2, 4, 3, 5, 0, 0, 0]

arr2 = [1, 2, 0, 0, 0, 3, 6]
push_zeros_to_end(arr2)
print("Modified array:", arr2)  # Output: [1, 2, 3, 6, 0, 0, 0]
