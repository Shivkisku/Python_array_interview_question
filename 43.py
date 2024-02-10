def reorder_elements(arr, index):
    # Create a list of tuples containing elements and their corresponding indices
    merged = list(zip(arr, index))
    
    # Sort the merged list based on the indices
    merged.sort(key=lambda x: x[1])
    
    # Extract the sorted elements and indices
    sorted_arr = [x[0] for x in merged]
    sorted_index = [x[1] for x in merged]
    
    return sorted_arr, sorted_index

# Example usage:
arr1 = [10, 11, 12]
index1 = [1, 0, 2]
sorted_arr1, sorted_index1 = reorder_elements(arr1, index1)
print("Sorted arr[]:", sorted_arr1)     # Output: [11, 10, 12]
print("Sorted index[]:", sorted_index1) # Output: [0, 1, 2]

arr2 = [50, 40, 70, 60, 90]
index2 = [3, 0, 4, 1, 2]
sorted_arr2, sorted_index2 = reorder_elements(arr2, index2)
print("Sorted arr[]:", sorted_arr2)     # Output: [40, 60, 90, 50, 70]
print("Sorted index[]:", sorted_index2) # Output: [0, 1, 2, 3, 4]
