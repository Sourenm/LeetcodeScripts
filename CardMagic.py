def main(n, k, t):
    combs = []
    pointer = n - 1
    current = [1 for x in range(n)]
    combs.append(current.copy())
    current[pointer] += 1
    combs.append(current.copy())
    while current[pointer] < k:
        current[pointer] += 1
        combs.append(current.copy())
    while len(combs) < (k ** n):
        pointer -= 1
        temp = combs.copy()
        while temp[0][pointer] < k:
            for i in range(len(temp)):
                temp[i][pointer] += 1
                combs.append(temp[i])
    count = 0
    for i in range(len(combs)):
        if sum(combs[i]) == t:
            count += 1
    print(count)
main(5, 2, 3)