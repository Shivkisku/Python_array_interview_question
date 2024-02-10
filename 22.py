def merge(arr, temp_arr, left, mid, right):
    i = left  # Initial index of first subarray
    j = mid + 1  # Initial index of second subarray
    k = left  # Initial index of merged subarray
    inversion_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            j += 1
            inversion_count += (mid - i + 1)  # Count inversions when element from the right subarray is smaller
        k += 1

    # Copy the remaining elements of left subarray if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of right subarray if any
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy back the merged elements to original array
    for index in range(left, right + 1):
        arr[index] = temp_arr[index]

    return inversion_count

def merge_sort(arr, temp_arr, left, right):
    inversion_count = 0
    if left < right:
        mid = (left + right) // 2
        # Recursively sort both halves and count inversions
        inversion_count += merge_sort(arr, temp_arr, left, mid)
        inversion_count += merge_sort(arr, temp_arr, mid + 1, right)
        # Merge the sorted halves and count inversions
        inversion_count += merge(arr, temp_arr, left, mid, right)
    return inversion_count

def inversion_count(arr):
    n = len(arr)
    temp_arr = [0] * n
    return merge_sort(arr, temp_arr, 0, n - 1)

# Example usage:
arr = [1, 20, 6, 4, 5]
print("Inversion count:", inversion_count(arr))  # Output: 5 (for the inversions (20,6), (20,4), (20,5), (6,4), (6,5))
