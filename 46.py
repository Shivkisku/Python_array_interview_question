def largest_number(arr):
    # Convert integers to strings for easy comparison
    arr = list(map(str, arr))

    # Custom comparison function for sorting
    def compare(a, b):
        return int(b + a) - int(a + b)

    # Sort the array based on the custom comparison function
    arr.sort(key=compare)

    # Concatenate the sorted numbers into a single string
    largest_num = ''.join(arr)

    return largest_num

# Example usage:
arr1 = [54, 546, 548, 60]
print("Largest number:", largest_number(arr1))  # Output: 6054854654

arr2 = [1, 34, 3, 98, 9, 76, 45, 4]
print("Largest number:", largest_number(arr2))  # Output: 998764543431
