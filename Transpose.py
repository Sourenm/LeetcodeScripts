def main(n, a):
    b = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(a[j][i])
        b.append(temp)
    for i in range(n):
        print(b[i])
main(3, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
