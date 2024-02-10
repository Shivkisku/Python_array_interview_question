# Function to perform MO's Algorithm
def mos_algorithm(arr, queries):
    n = len(arr)
    q = len(queries)
    block_size = int(n ** 0.5)  # Size of each block

    # Function to sort queries based on block number
    def custom_sort(query):
        return query[0] // block_size, query[1]

    # Sort the queries
    queries.sort(key=custom_sort)

    # Initialize variables
    current_sum = 0
    left, right = 0, -1

    # Process each query
    for query in queries:
        l, r = query

        # Extend current range to include elements of the new query
        while right < r:
            right += 1
            current_sum += arr[right]

        # Shrink current range to exclude elements of the old query
        while left < l:
            current_sum -= arr[left]
            left += 1

        # Shrink current range to exclude elements of the new query
        while left > l:
            left -= 1
            current_sum += arr[left]

        # Output result for the current query
        print("Sum of arr[] elements in range", query, "is", current_sum)

# Example usage:
arr = [1, 1, 2, 1, 3, 4, 5, 2, 8]
queries = [[0, 4], [1, 3], [2, 4]]
mos_algorithm(arr, queries)
