#You are given an array A with size N (indexed from 0) and an integer K. Let's define another array B with size N · K as the array that's formed by concatenating K copies of array A.

#For example, if A = {1, 2} and K = 3, then B = {1, 2, 1, 2, 1, 2}.

#You have to find the maximum subarray sum of the array B. Fomally, you should compute the maximum value of Bi + Bi+1 + Bi+2 + ... + Bj, where 0 ≤ i ≤ j < N · K.


def max_subarray_sum(arr):
    max_ending_here = max_so_far = arr[0]
    for x in arr[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

def max_subarray_sum_concatenated(A, K):
    # Concatenate K copies of array A
    B = A * K
    
    # Find the maximum subarray sum of B using Kadane's algorithm
    return max_subarray_sum(B)

# Example usage
A = [1, 2]
K = 3
print(max_subarray_sum_concatenated(A, K))  # Output will be 9 for the example provided
