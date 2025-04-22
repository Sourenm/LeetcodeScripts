def main(n, p, d):
    collection_p = []
    collection_d = []
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            collection_p.append(p[i: j + 1])
            collection_d.append(d[i: j + 1])
    max_d = 2
    for i in range(len(collection_p)):
        if collection_p[i][0] in d:
            first = d.index(collection_p[i][0])
            flag = 0
            if first + len(collection_p[i]) < len(d):
                for j in range(first, len(collection_p[i]) + first):
                    if collection_p[i][j - first] != d[j]:
                        flag = 1
                        break
                if flag == 0:
                    max_d = len(collection_p[i])
    for i in range(len(collection_d)):
        if collection_d[i][0] in p:
            first = p.index(collection_d[i][0])
            flag = 0
            if first + len(collection_d[i]) < len(p):
                for j in range(first, len(collection_d[i]) + first):
                    if collection_d[i][j - first] != p[j]:
                        flag = 1
                        break
                if flag == 0:
                    max_d = len(collection_d[i])
    print(max_d)
    print(collection_p)
    print(collection_d)

n_sample = 6
p_sample = [0, 1, 2, 3, 4, 5]
d_sample = [1, 2, 0, 3, 4, 5]
main(n_sample, p_sample, d_sample)
