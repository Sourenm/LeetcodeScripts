def main(n):
    i = 1
    b = 1
    j = 0
    while n[j] <= 0:
        j += 1
    while i <= n[j]:
        b *= i
        i += 1
    print(b)
n_sample = [5, -3, 8, 0, 4]
main(n_sample)
