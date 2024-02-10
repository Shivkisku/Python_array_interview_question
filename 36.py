def next_permutation(nums):
    # Step 1: Find the largest index i such that nums[i] < nums[i + 1]
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    
    # If no such index exists, reverse the entire array
    if i == -1:
        nums.reverse()
        return
    
    # Step 2: Find the largest index j greater than i such that nums[j] > nums[i]
    j = len(nums) - 1
    while nums[j] <= nums[i]:
        j -= 1
    
    # Step 3: Swap nums[i] and nums[j]
    nums[i], nums[j] = nums[j], nums[i]
    
    # Step 4: Reverse the subarray nums[i + 1:]
    nums[i + 1:] = reversed(nums[i + 1:])

# Example usage:
nums1 = [1, 2, 3]
next_permutation(nums1)
print("Next permutation:", nums1)  # Output: [1, 3, 2]

nums2 = [2, 3, 1]
next_permutation(nums2)
print("Next permutation:", nums2)  # Output: [3, 1, 2]

nums3 = [3, 2, 1]
next_permutation(nums3)
print("Next permutation:", nums3)  # Output: [1, 2, 3]
