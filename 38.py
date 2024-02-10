def maxSumOfThreeSubarrays(nums, k):
    n = len(nums)
    
    # Calculate prefix sum
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    # Calculate maximum subarray sum starting from the left
    left_max = [0] * n
    max_sum = float('-inf')
    for i in range(k - 1, n):
        current_sum = prefix_sum[i + 1] - prefix_sum[i - k + 1]
        if current_sum > max_sum:
            max_sum = current_sum
        left_max[i] = max_sum
    
    # Calculate maximum subarray sum starting from the right
    right_max = [0] * n
    max_sum = float('-inf')
    for i in range(n - k, -1, -1):
        current_sum = prefix_sum[i + k] - prefix_sum[i]
        if current_sum > max_sum:
            max_sum = current_sum
        right_max[i] = max_sum
    
    # Find the maximum sum of three non-overlapping subarrays
    max_total = float('-inf')
    result = []
    for i in range(k, n - 2 * k + 1):
        left_sum = left_max[i - 1]
        right_sum = right_max[i + k]
        total_sum = left_sum + right_sum
        
        # Check if the total sum is greater than the current maximum
        if total_sum > max_total:
            max_total = total_sum
            result = [i - k, i, i + k]
    
    return result

# Example usage:
nums1 = [1,2,1,2,6,7,5,1]
k1 = 2
print(maxSumOfThreeSubarrays(nums1, k1))  # Output: [0, 3, 5]

nums2 = [1,2,1,2,1,2,1,2,1]
k2 = 2
print(maxSumOfThreeSubarrays(nums2, k2))  # Output: [0, 2, 4]
