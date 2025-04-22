from math import sqrt
def main(n, q, p):
    primes = []
    for i in range(2, n + 1):
        flag = 0
        for j in range(2, int(sqrt(i)) + 1):
            if i % j == 0 and i != j:
                flag = 1
                break
        if flag == 0:
            primes.append(i)
    print(len(primes))
    for i in range(q):
        if p[i] in primes:
            print(1)
        else:
            print(0)
n = 20
q = 5
p = [2, 5, 7, 10, 12]
main(n, q, p)