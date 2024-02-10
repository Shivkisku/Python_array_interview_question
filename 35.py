def generate_arrays(A, B, i, j, current_array, result):
    if i == len(A) and j == len(B) - 1:
        result.append(current_array[:])
        return
    
    if i < len(A):
        current_array.append(A[i])
        generate_arrays(A, B, i + 1, j, current_array, result)
        current_array.pop()
    
    if j < len(B) - 1:
        current_array.append(B[j])
        generate_arrays(A, B, i, j + 1, current_array, result)
        current_array.pop()

def generate_possible_arrays(A, B):
    result = []
    generate_arrays(A, B, 0, 0, [], result)
    return result

# Example usage:
A = [1, 2]
B = [3, 4]
print("Possible arrays:", generate_possible_arrays(A, B))
