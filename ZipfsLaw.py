def main(n, m, temp):
    scores = []
    names = []
    for i in range(n):
        names.append(temp[i][1])
        scores.append(int(temp[i][0]) * i)
    for i in range(m):
        print(names[scores.index(max(scores))])
        names.pop(scores.index(max(scores)))
        scores.pop(scores.index((max(scores))))

n = 2
m = 2
temp = [
    (4, 'Alice'),
    (2, 'Bob'),
]
main(n, m, temp)