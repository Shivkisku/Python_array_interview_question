import heapq

def k_smallest_pairs(arr1, arr2, k):
    if not arr1 or not arr2:
        return []
    
    heap = []
    
    # Push the initial pairs (arr1[0], arr2[i]) for each i in range(len(arr2))
    for i in range(min(k, len(arr2))):
        heapq.heappush(heap, (arr1[0] + arr2[i], 0, i))
    
    result = []
    while heap and k > 0:
        # Pop the pair with the smallest sum
        s, i, j = heapq.heappop(heap)
        result.append((arr1[i], arr2[j]))
        k -= 1
        
        # Push the next pair (arr1[i+1], arr2[j]) if available
        if i + 1 < len(arr1):
            heapq.heappush(heap, (arr1[i + 1] + arr2[j], i + 1, j))
    
    return result

# Example usage
arr1 = [1, 7, 11]
arr2 = [2, 4, 6]
k = 3
print("k pairs with smallest sums:", k_smallest_pairs(arr1, arr2, k))
