def minimize_height_difference(towers, k):
    # Sort the array of tower heights
    towers.sort()
    
    # Initialize the initial difference between the tallest and shortest tower
    initial_diff = towers[-1] - towers[0]
    
    # Increase the height of each tower by K and find the new difference
    increased_diff = towers[-1] - k - (towers[0] + k)
    
    # Decrease the height of each tower by K and find the new difference
    decreased_diff = towers[-1] - k - (towers[0] - k)
    
    # Return the minimum difference found
    return min(initial_diff, increased_diff, decreased_diff)

# Example usage:
towers = [1, 5, 8, 10]
k = 2
print("Minimum height difference:", minimize_height_difference(towers, k))  # Output: 5
