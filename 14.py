def search_in_rotated_array(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # If the key is found at the middle position
        if arr[mid] == key:
            return mid

        # If the left half is sorted
        if arr[low] <= arr[mid]:
            # Check if the key lies in the left half
            if arr[low] <= key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        # If the right half is sorted
        else:
            # Check if the key lies in the right half
            if arr[mid] < key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

# Example usage
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 6
index = search_in_rotated_array(arr, key)
if index != -1:
    print("Key", key, "found at index", index)
else:
    print("Key", key, "not found in the array")
