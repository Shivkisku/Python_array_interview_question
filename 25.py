def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]
    for interval in intervals[1:]:
        # If the current interval overlaps with the previous merged interval, merge them
        if interval[0] <= merged[-1][1]:
            merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        else:
            merged.append(interval)

    return merged

# Example usage:
intervals1 = [[1, 3], [2, 4], [6, 8], [9, 10]]
print("Merged intervals:", merge_intervals(intervals1))  # Output: [[1, 4], [6, 8], [9, 10]]

intervals2 = [[6, 8], [1, 9], [2, 4], [4, 7]]
print("Merged intervals:", merge_intervals(intervals2))  # Output: [[1, 9]]
