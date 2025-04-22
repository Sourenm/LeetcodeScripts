import math
def main(n):
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print('1', end=' ')
            else:
                print(int(math.factorial(i - 1) / (math.factorial(j - 1) * math.factorial(i - j))), end=' ')
        print()
main(4)
