def main(n, m, st, temp):
    d = {}
    for i in range(m):
        if temp[i][0] not in d:
            d[temp[i][0]] = []
        if temp[i][1] not in d:
            d[temp[i][1]] = []
        if temp[i][1] not in d[temp[i][0]]:
            d[temp[i][0]].append(temp[i][1])
        if temp[i][0] not in d[temp[i][1]]:
            d[temp[i][1]].append(temp[i][0])
        for j in d.keys():
            for k in d.keys():
                if j != k:
                    for value in d[j]:
                        if value not in d[k] and value != k and j in d[k]:
                            d[k].append(value)
                    for value in d[j]:
                        if value not in d[j] and value != j and k in d[j]:
                            d[j].append(value)
    size = 0
    for i in range(len(st)):
        if st[i] in d:
            temp = st[i]
            for j in range(len(d[st[i]])):
                if len(d[st[i]][j]) < len(temp):
                    temp = d[st[i]][j]
            st[i] = temp
        size += len(st[i])
    print(st)
    print(size)
main(4, 3, ["apple", "banana", "cherry", "date"], [("apple", "banana"), ("banana", "cherry"), ("date", "apple")])
