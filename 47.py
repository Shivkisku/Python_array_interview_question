def mark_multiples_of_2_and_5(a, b):
    # Initialize a bitmask to store multiples of 2 and 5
    bitmask = 0

    # Mark multiples of 2 and 5 between a and b
    for num in range(a, b + 1):
        if num % 2 == 0:
            bitmask |= 1 << (num - a)
        if num % 5 == 0:
            bitmask |= 1 << (num - a)

    # Output each multiple of 2 and 5
    for num in range(a, b + 1):
        if bitmask & (1 << (num - a)):
            if num % 2 == 0:
                print(num, "is a multiple of 2")
            if num % 5 == 0:
                print(num, "is a multiple of 5")

# Example usage:
a = 10
b = 30
mark_multiples_of_2_and_5(a, b)
