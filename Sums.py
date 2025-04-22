def main(n, a):
    b = []
    sum_r = []
    sum_c = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(a[j][i])
        b.append(temp)
    for i in range(n):
        sum_r.append(sum(a[i]))
        sum_c.append(sum(b[i]))
    for i in range(n):
        print(str(a[i]) + '|' + str(sum_r[i]))
    print('---------')
    sum_c.append(sum(sum_r))
    print(sum_c)
n = 3
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
main(n, a)