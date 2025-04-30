def buy_sell(prices):
    ind_buy = 0
    ind_sell = 0
    running_max = 0
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > running_max:
                ind_buy = i
                ind_sell = j
                running_max = prices[j] - prices[i]
    return running_max

prices = [7,6,4,3,1]
print(buy_sell(prices))