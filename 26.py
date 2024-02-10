def max_profit(prices):
    if not prices:
        return 0
    
    n = len(prices)
    # Initialize arrays to store maximum profit with at most k transactions
    max_profit1 = [0] * n
    max_profit2 = [0] * n
    
    # Initialize variables to store the minimum price and maximum profit for the first transaction
    min_price = prices[0]
    max_profit = 0
    
    # Calculate maximum profit for the first transaction
    for i in range(1, n):
        max_profit = max(max_profit, prices[i] - min_price)
        max_profit1[i] = max_profit
        min_price = min(min_price, prices[i])
    
    # Initialize variable to store the maximum price and maximum profit for the second transaction
    max_price = prices[-1]
    max_profit = 0
    
    # Calculate maximum profit for the second transaction
    for i in range(n - 2, -1, -1):
        max_profit = max(max_profit, max_price - prices[i])
        max_profit2[i] = max_profit
        max_price = max(max_price, prices[i])
    
    # Calculate the maximum profit by considering all possible combinations of two transactions
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, max_profit1[i] + max_profit2[i])
    
    return max_profit

# Example usage:
prices1 = [10, 22, 5, 75, 65, 80]
print("Maximum profit:", max_profit(prices1))  # Output: 87

prices2 = [2, 30, 15, 10, 8, 25, 80]
print("Maximum profit:", max_profit(prices2))  # Output: 100
