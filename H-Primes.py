def main(n):
    i = 1
    count = 0
    results = []
    while (4 * i + 1) <= n:
        check = 4 * i + 1
        for j in range(1, i):
            div = 4 * j + 1
            if check % div == 0:
                if (check / div) % 4 == 1:
                    count += 1
                    results.append(check)
                    break
        i += 1
    print(count)
    print(results)
n_sample = 30
main(n_sample)