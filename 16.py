def search_in_rotated_array(arr, key):
    # Function to perform binary search
    def binary_search(arr, low, high, key):
        while low <= high:
            mid = (low + high) // 2

            # If the key is found at the middle itself
            if arr[mid] == key:
                return mid

            # If the left half is sorted
            if arr[low] <= arr[mid]:
                if arr[low] <= key <= arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # If the right half is sorted
            else:
                if arr[mid] <= key <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1

    # Call binary search function
    return binary_search(arr, 0, len(arr) - 1, key)

# Example usage:
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 6
index = search_in_rotated_array(arr, key)
if index != -1:
    print("Key", key, "found at index", index)
else:
    print("Key", key, "not found in the array.")
