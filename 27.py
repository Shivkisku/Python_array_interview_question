def max_profit(prices, k):
    if not prices:
        return 0
    
    n = len(prices)
    # If the number of transactions allowed is greater than or equal to half the length of the prices array,
    # it means we can make as many transactions as we want, so we use the greedy approach to find the maximum profit
    if k >= n // 2:
        max_profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit
    
    # Initialize a 2D array to store maximum profit with at most k transactions
    dp = [[0] * n for _ in range(k + 1)]
    
    # Calculate maximum profit for each number of transactions from 1 to k
    for i in range(1, k + 1):
        max_diff = -prices[0]
        for j in range(1, n):
            # Calculate maximum profit by either not doing any transaction on day j
            # or by selling on day j with a transaction on day t, where 0 <= t < j
            dp[i][j] = max(dp[i][j - 1], max_diff + prices[j])
            # Update max_diff to consider buying on day j with a transaction on day t, where 0 <= t < j
            max_diff = max(max_diff, dp[i - 1][j] - prices[j])
    
    return dp[k][n - 1]

# Example usage:
prices1 = [10, 22, 5, 75, 65, 80]
k1 = 2
print("Maximum profit:", max_profit(prices1, k1))  # Output: 87

prices2 = [12, 14, 17, 10, 14, 13, 12, 15]
k2 = 3
print("Maximum profit:", max_profit(prices2, k2))  # Output: 12

prices3 = [100, 30, 15, 10, 8, 25, 80]
k3 = 3
print("Maximum profit:", max_profit(prices3, k3))  # Output: 72

prices4 = [90, 80, 70, 60, 50]
k4 = 1
print("Maximum profit:", max_profit(prices4, k4))  # Output: 0
