def generate_combinations(arr, r, idx=0, combination=[]):
    if len(combination) == r:
        print(" ".join(map(str, combination)))
        return
    
    for i in range(idx, len(arr)):
        generate_combinations(arr, r, i + 1, combination + [arr[i]])

# Example usage:
arr = [1, 2, 3, 4]
r = 2
generate_combinations(arr, r)
