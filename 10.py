## Given an array of N non-negative integers arr[] representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

def trap_water(arr):
    n = len(arr)
    if n <= 2:
        return 0
    
    left, right = 0, n - 1
    left_max = arr[left]
    right_max = arr[right]
    water_trapped = 0

    while left < right:
        if arr[left] <= arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water_trapped += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water_trapped += right_max - arr[right]
            right -= 1

    return water_trapped

# Example usage
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print("Amount of water trapped:", trap_water(arr))
