def main(n, m, r):
    round = 0
    for i in range(m):
        if r[i] > 0:
            round += 1
    result = [0 for x in range(m)]
    while n > round:
        for i in range(len(r)):
            if r[i] > 1:
                r[i] -= 1
                result[i] += 1
                n -= 1
            elif r[i] == 1:
                r[i] = 0
                result[i] += 1
                round -= 1
                n -= 1
    for i in range(len(result)):
        if n > 0 and r[i] != 0:
            r[i] -= 1
            result[i] += 1
            n -= 1
        elif n == 0:
            break
    print(result)
n = 7
m = 3
r = [3, 1, 4]
main(n, m, r)
