def main(n, m, temp):
    d = {}
    for i in range(m):
        d[temp[i][0]] = temp[i][1]
    while len(d) > 0:
        books = []
        cycle = []
        for i in d.keys():
            books.append(d[i])
            cycle.append(i)
            flag = 0
            for j in books:
                if d[j] in books:
                    flag = 1
                    break
                else:
                    cycle.append(j)
                    books.append(d[j])
            if flag == 1:
                break
        if flag == 1 and sorted(cycle) == sorted(books):
            for i in range(len(cycle)):
                d.pop(cycle[i])
        if flag == 1 and sorted(cycle) != sorted(books):
            print('No')
            break
    if (len(d)) == 0:
        print('YES')
n = 5
m = 4
temp = [
    (1, 2),
    (2, 3),
    (3, 4),
    (4, 2),
]
main(n, m, temp)
