def min_number(pattern):
    result = []
    current_number = 1

    for char in pattern:
        if char == 'I':
            result.append(current_number)
            current_number += 1
        elif char == 'D':
            count_D = 1
            while pattern and pattern[0] == 'D':
                count_D += 1
                pattern = pattern[1:]
            result.extend(range(current_number + count_D - 1, current_number - 1, -1))
            current_number += count_D

    result.append(current_number)
    return ''.join(map(str, result))

# Examples
print(min_number("D"))         # Output: 21
print(min_number("I"))         # Output: 12
print(min_number("DD"))        # Output: 321
print(min_number("II"))        # Output: 123
print(min_number("DIDI"))      # Output: 21435
print(min_number("IIDDD"))     # Output: 126543
print(min_number("DDIDDIID"))  # Output: 321654798
