def main(n, prices, check):
    count = 0
    for i in range(n):
        for j in range(i + 1):
            p = sum(prices[j: i + 1]) / len(prices[j: i + 1])
            if  p >= check:
                count += 1
    print(count)
n = 5
prices = [10.0, 15.0, 20.0, 25.0, 30.0]
check = 18.0
main(n, prices, check)
