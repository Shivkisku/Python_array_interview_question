def maxCircularSum(arr, n):
    if n == 1:
        return arr[0]

    total_sum = sum(arr)
    max_sum = arr[0]
    current_max = arr[0]
    min_sum = arr[0]
    current_min = arr[0]

    for i in range(1, n):
        current_max = max(current_max + arr[i], arr[i])
        max_sum = max(max_sum, current_max)

        current_min = min(current_min + arr[i], arr[i])
        min_sum = min(min_sum, current_min)

    if min_sum == total_sum:
        return max_sum

    return max(max_sum, total_sum - min_sum)

# Example usage:
arr = [11, 10, -20, 5, -3, -5, 8, -13, 10]
n = len(arr)
print("Maximum circular sum is", maxCircularSum(arr, n))
