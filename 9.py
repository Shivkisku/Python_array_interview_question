## Given the arrival and departure times of all trains that reach a railway station, the task is to find the minimum number of platforms required for the railway station so that no train waits. We are given two arrays that represent the arrival and departure times of trains that stop.



def min_platforms(arrival, departure):
    n = len(arrival)
    arrival.sort()
    departure.sort()
    
    platforms_needed = 1
    result = 1
    i = 1
    j = 0
    
    while i < n and j < n:
        if arrival[i] <= departure[j]:
            platforms_needed += 1
            i += 1
            result = max(result, platforms_needed)
        else:
            platforms_needed -= 1
            j += 1
    
    return result

# Example usage
arrival = [900, 940, 950, 1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
print("Minimum number of platforms required:", min_platforms(arrival, departure))
