from math import sqrt
def main(n, m):
    not_prime_n = 0
    not_prime_m = 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            not_prime_n = 1
            break
    for i in range(2, int(sqrt(m)) + 1):
        if m % i == 0:
            not_prime_m = 1
            break
    if m != n and not_prime_n == 0 and not_prime_m == 0:
        print('Full Credit')
    else:
        checker = m * n
        flag = 0
        counter = 4
        step = 2
        while counter <= checker:
            if checker % counter == 0:
                if sqrt(counter) == int(sqrt(counter)):
                    print('No Credit')
                    flag = 1
                    break
            step += 1
            counter = step ** 2
        if flag == 0:
            print('Partial Credit')
main(4, 4)