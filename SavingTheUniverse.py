def main(n, d, q, queries):
    for i in range(q):
        if d[queries[i][-1]] == -1:
            d[queries[i][-1]] = len(queries)
    switches = 0
    while len(queries) > 0:
        mx_ind = 0
        flag = 0
        for k, v in d.items():
            if v == -1:
                flag = 1
                break
            else:
                if v > mx_ind:
                    mx_ind = v
                d[k] = -1
        if flag == 1:
            break
        else:
            switches += 1
            for i in range(mx_ind - 1):
                queries.pop(0)
            for i in range(len(queries)):
                if d[queries[i]] == -1:
                    d[queries[i]] = i
    
    print(switches)
    

n = 5
d = {1: 2, 2: 5, 3: 3, 4: -1, 5: 4}
q = 4
queries = [
    [1, 2],
    [3],
    [5],
    [4, 1],
]
main(n, d, q, queries)
