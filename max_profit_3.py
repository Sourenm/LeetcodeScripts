def max_profit_3(prices):
    tuples = []
    running_max = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > running_max:
                running_max = prices[j] - prices[i]
            tuples.append((prices[i], prices[j]))
    final = sorted(tuples, key=lambda x: x[1] - x[0], reverse=True)
    for i in range(1, len(final)):
        if prices.index(final[i - 1][0]) < prices.index(final[i][0]) and prices.index(final[i - 1][1]) < prices.index(final[i][0]) or prices.index(final[i][0]) < prices.index(final[i - 1][0]) and prices.index(final[i][1]) < prices.index(final[i - 1][0]):
            return max(running_max, final[i - 1][1] - final[i - 1][0] + final[i][1] - final[i][0])
    return 0

prices = [1,2,3,4,5]
print(max_profit_3(prices))