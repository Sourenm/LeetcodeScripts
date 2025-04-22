def main():
    M = 1
    q = 0
    d = 0
    n = 0
    p = 0
    sum = 0
    while M <= 100:
        change = M
        q = 0
        d = 0
        n = 0
        p = 0
        q = change // 25
        change -= q * 25
        d = change // 10
        change -= d * 10
        n = change // 5
        change -= n * 5
        p = change
        sum += q + d + n + p
        M = M + 1
    print('Average Number of Coins Equals: ', sum / 100)

main()