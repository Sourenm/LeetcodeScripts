def main(n, current):
    d = {}
    match = [0 for x in range(n)]
    for i in range(n):
        d[i] = []
        current[i] -= 1
        d[i].append(current[i])
        if current[i] == i:
            match[i] = 1
    if sum(match) == n:
        print('All Can Eat')
    else:
        while sum(match) != n:
            next = []
            next_match = []
            flag = 0
            for i in range(n):
                if match[i] != 1:
                    next.append(current[current[i]])
                else:
                    next.append(current[i])
                if next[i] == i:
                    next_match.append(1)
                else:
                    next_match.append(0)
                if next[i] not in d[i]:
                    d[i].append(next[i])
                else:
                    flag = 1
                    break
            match = next_match.copy()
            current = next.copy()
            if flag == 1:
                print('Some May Starve!')
                break
        if flag == 0:
            print('All May Eat!')

n = 5
current = [2, 0, 3, 1, 4]
main(n, current)