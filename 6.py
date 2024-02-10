## Given an array of distinct elements of size N, the task is to rearrange the elements of the array in a zig-zag fashion so that the converted array should be in the below form: 

    ## arr[0] < arr[1]  > arr[2] < arr[3] > arr[4] < . . . . arr[n-2] < arr[n-1] > arr[n]. 


def zigzag_arrangement(arr):
    n = len(arr)
    # Flag variable to indicate whether the next element should be greater or smaller
    flag = True

    for i in range(n - 1):
        if flag:
            # If flag is True, expect arr[i] < arr[i+1]
            if i % 2 == 0 and arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            elif i % 2 != 0 and arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            # If flag is False, expect arr[i] > arr[i+1]
            if i % 2 == 0 and arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            elif i % 2 != 0 and arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        flag = not flag

    return arr

# Example usage
arr = [4, 3, 7, 8, 6, 2, 1]
result = zigzag_arrangement(arr)
print("Zigzag arranged array:", result)
