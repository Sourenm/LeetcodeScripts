def main(a, n, b, m):    
    k = n * m
    print(k, end=' ')
    for i in range(1, k):
        if i % n == a % n and i % m == b % m:
            print(i)
            break
a = 3
n = 5
b = 2
m = 7
main(a, n, b, m)
