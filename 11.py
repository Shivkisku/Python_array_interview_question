## The cost of a stock on each day is given in an array. Find the maximum profit that you can make by buying and selling on those days. If the given array of prices is sorted in decreasing order, then profit cannot be earned at all.

def max_profit(prices):
    if len(prices) < 2:
        return 0
    
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        # Update the minimum price seen so far
        min_price = min(min_price, price)
        # Update the maximum profit that can be obtained
        max_profit = max(max_profit, price - min_price)

    return max_profit

# Example usage
prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]

print("Maximum profit from prices1:", max_profit(prices1))  # Output: 5
print("Maximum profit from prices2:", max_profit(prices2))  # Output: 0
