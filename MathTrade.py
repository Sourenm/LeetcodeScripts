def main(n, temp):
    has = []
    want = []
    for i in range(n):
        has.append(temp[i][1])
        want.append(temp[i][2])
    max_chain = 0
    counter = 0
    while counter < n:
        chain = 0
        flag = 0
        visited = [0 for x in range(n)]
        visited[counter] = 1
        current_has = []
        current_has.append(has[counter])
        current_want = []
        current_want.append(want[counter])
        for i in range(len(has)):
            if i != counter:
                if has[i] in current_want:
                    visited[i] = 1
                    current_has.append(has[i])
                    current_want.append(want[i])
                    for j in range(0, i):
                        if has[j] in current_want and visited[j] == 0:
                            current_has.append(has[j])
                            current_want.append(want[j])
        if sorted(current_has) == sorted(current_want):
            if len(current_has) > max_chain:
                max_chain = len(current_has)
        counter += 1
    if max_chain != 0:
        print(max_chain)
    else:
        print('No Trades Possible')

n = 4
temp = [(0, 1, 2), (1, 2, 3), (2, 3, 4), (4, 5, 6)]
main(n, temp)