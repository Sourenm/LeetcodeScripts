from math import factorial as f
def main(n, k):
    result = f(n) / (f(k) * f(n - k))
    count = 0
    for i in range(1, int(result) + 1):
        if result % i == 0:
            count += 1
    print(count)
n_sample = 5
k_sample = 2
main(n_sample, k_sample)
