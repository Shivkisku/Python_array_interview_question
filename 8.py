## Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

    ## Each student gets one packet.
    ## The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.


def min_difference_chocolates(arr, m):
    if m == 0 or len(arr) == 0:
        return 0
    
    n = len(arr)
    if n < m:
        return -1  # Not enough packets for all students
    
    arr.sort()  # Sort the array of chocolate packets
    
    min_diff = float('inf')  # Initialize minimum difference
    
    # Iterate through the array with a sliding window of size m
    for i in range(n - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])
    
    return min_diff

# Example usage
arr = [7, 3, 2, 4, 9, 12, 56]
m = 3
result = min_difference_chocolates(arr, m)
print("Minimum difference between maximum and minimum chocolates:", result)
