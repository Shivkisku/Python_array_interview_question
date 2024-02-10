##Given an array of n positive integers. Write a program to find the sum of maximum sum subsequence of the given array such that the integers in the subsequence are sorted in increasing order. For example, if input is {1, 101, 2, 3, 100, 4, 5}, then output should be 106 (1 + 2 + 3 + 100), if the input array is {3, 4, 5, 10}, then output should be 22 (3 + 4 + 5 + 10) and if the input array is {10, 5, 4, 3}, then output should be 10


def max_sum_increasing_subsequence(arr):
    n = len(arr)
    # Initialize a list to store the maximum sum of increasing subsequence ending at each index
    max_sum = arr[:]
    
    # Iterate through each element in the array
    for i in range(1, n):
        # Compare the current element with all previous elements to find the maximum sum of increasing subsequence
        for j in range(i):
            if arr[i] > arr[j] and max_sum[i] < max_sum[j] + arr[i]:
                max_sum[i] = max_sum[j] + arr[i]
    
    # Return the maximum sum of increasing subsequence
    return max(max_sum)

# Example usage
arr1 = [1, 101, 2, 3, 100, 4, 5]
arr2 = [3, 4, 5, 10]
arr3 = [10, 5, 4, 3]

print("Maximum sum of increasing subsequence:", max_sum_increasing_subsequence(arr1))  # Output: 106
print("Maximum sum of increasing subsequence:", max_sum_increasing_subsequence(arr2))  # Output: 22
print("Maximum sum of increasing subsequence:", max_sum_increasing_subsequence(arr3))  # Output: 10
