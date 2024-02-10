def maximum_possible_sum(T, test_cases):
    for _ in range(T):
        N, sequences = test_cases[_]
        sequences.sort()

        current_max = sequences[-1][-1]  # Initialize current_max with the largest element of the last sequence

        total_sum = current_max
        for i in range(N - 2, -1, -1):
            idx = -1
            for j in range(N):
                if sequences[i][j] < current_max:
                    idx = j
                else:
                    break

            if idx == -1:
                print(-1)
                break

            current_max = sequences[i][idx]
            total_sum += current_max

        else:
            print(total_sum)

# Example usage:
T = 2
test_cases = [
    (3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
    (3, [[9, 8, 7], [6, 5, 4], [3, 2, 1]])
]

maximum_possible_sum(T, test_cases)
