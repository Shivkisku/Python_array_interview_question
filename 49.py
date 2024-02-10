def iterative_subset(array):
    array_length = len(array)
    result = []
    
    for j in range(array_length):
        i = j
        sets = set()
        
        while array[i] not in sets:
            i = array[i]
            sets.add(i)
        
        result.append(list(sets))
    
    return result

# Example usage:
array = [5, 6, 3, 1, 4, 7, 8, 9, 2, 11, 12, 2, 4, 6, 9, 4, 1]
print(iterative_subset(array))
