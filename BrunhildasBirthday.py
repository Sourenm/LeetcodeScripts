def main(m, q, calls, check):
    for i in range(q):
        total = 0
        flag = 0
        while True:
            max_remove = 0
            max_ind = 0
            for j in range(len(calls)):
                if check[i] % calls[j] > max_remove:
                    max_remove = check[i] % calls[j]
                    max_ind = j
            if max_remove == 0:
                print('oo')
                flag = 1
                break
            total += 1
            if check[i] % calls[max_ind] == check[i]:
                print(total + 1)
                break
            check[i] %= calls[max_ind]
main(2, 2, [1, 2], [1, 2])