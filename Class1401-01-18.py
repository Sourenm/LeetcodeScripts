def main(n, a, b):
    temp = []
    final = []
    for i in range(n):
        temp = []
        for j in range(len(a[0])):
            temp.append(a[i][j] + b[i][j])
        final.append(temp)
    for i in range(n):
        print(final[i])
n = 3
a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1],
]
main(n, a, b)