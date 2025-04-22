def main(n, q, query):
    set = [[] for x in range(n)]
    for i in range(n):
        set[i].append(str(i))
    for i in range(q):
        flag = 0
        if query[i][0] == '?':
            for i in range(len(set)):
                if query[i][1] in set[i] and query[i][2] in set[i]:
                    print('Yes')
                    flag = 1
                    break
            if flag == 0:
                print('No')
        if query[i][0] == '=':
            for j in range(len(set)):
                if query[i][1] in set[j] and query[i][2] not in set[j]:
                    set[j].append(query[i][2])
                    if query[i][2] in set:
                        set.pop(set.index(query[i][2]))
                    break
                elif query[i][2] in set[j] and query[i][1] not in set[j]:
                    set[j].append(query[i][1])
                    set.pop(set.index([query[i][1]]))
                    break
n = 3
q = 3
query = [
    ('?', '1', '2'),
    ('=', '1', '3'),
    ('?', '2', '3'),
]
main(n, q, query)
