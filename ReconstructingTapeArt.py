def main(n, art):
    flag = 0
    d = {}
    for i in range(n):
        if art[i] not in d.keys():
            first_index = i
            last_index = 0
            for j in range(n - 1, 0, -1):
                if art[j] == art[i]:
                    last_index = j
                    break
            if first_index != last_index:
                temp = art[first_index : last_index + 1].copy()
                for j in range(first_index):
                    if temp.count(art[j]) > 0:
                        print('IMPOSSIBLE')
                        flag = 1
                        break
                for j in range(last_index + 1, n):
                    if temp.count(art[j]) > 0:
                        print('IMPOSSIBLE')
                        flag = 1
                        break
                if flag == 1:
                    break
            d[art[i]] = []
            d[art[i]].append(first_index + 1)
            d[art[i]].append(last_index + 1)
    if flag != 1:
        print(len(d.keys()))
        for k, v in d.items():
            print(f'{v[0]} {v[1]} {k}')
n = 8
art = [1, 2, 3, 4, 2, 5, 6, 3]
main(n, art)