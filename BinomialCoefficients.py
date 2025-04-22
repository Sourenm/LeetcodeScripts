from math import factorial as f
def main(n):
    k = 1
    m = 1
    count = 0
    while m < n and k < n:
        check = f(m) / (f(k) * f(m - k))
        if check % 2 != 0:
            count += 1
        if k == m:
            m += 1
            k = 1
        else:
            k += 1
    print(count)

main(10)