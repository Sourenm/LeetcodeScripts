def main(n):
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            print(i - 1, end=' ')
    print(n - 1)
n = 12
main(n)