def main(n, k, prices):
    max_profit = 0
    for i in range(n):
        for j in range(i + 1, n):
            profit = (100 * (prices[i] - prices[j])) - (k * (j - i))
            if profit > max_profit:
                max_profit = profit
    
    print(max_profit)
n = 5
k = 2
prices = [4.0, 3.0, 7.0, 6.0, 8.0]
main(n, k, prices)
