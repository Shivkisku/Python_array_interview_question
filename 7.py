## Given an unsorted array and a number n, find if there exists a pair of elements in the array whose difference is n. 

def find_pair_with_difference(arr, n):
    # Create a set to store elements of the array
    elements_set = set(arr)
    
    # Iterate through the array
    for num in arr:
        # Check if num + n or num - n exists in the set
        if num + n in elements_set or num - n in elements_set:
            return True
    
    # If no such pair is found, return False
    return False

# Example usage
arr = [5, 20, 3, 2, 50, 80]
n = 78
result = find_pair_with_difference(arr, n)
if result:
    print("There exists a pair of elements in the array whose difference is", n)
else:
    print("No such pair exists")
