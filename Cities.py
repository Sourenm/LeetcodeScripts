def main(n, m, temp):
    lines = []
    for i in range(m):
        lines.append([0, 0])
    for i in range(m):
        lines[i][0] = temp[i][0]
        lines[i][1] = temp[i][1]
    graph = []
    temp = []
    for i in range(n):
        temp.append(0)
    for i in range(n):
        graph.append(temp.copy())
    for i in range(len(lines)):
        row = (lines[i][0]) - 1
        col = (lines[i][1]) - 1
        graph[row][col] = 1
        graph[col][row] = 1
    flag = 0
    for i in range(len(graph)):
        count = 0
        for j in range(len(graph[i])):
            count += graph[i][j]
        if count < 2:
            flag = 1
            print('Impossible!')
            break
    if flag == 0:
        path = []
        path.append(1)
        i = 0
        while True:
            if len(path) == len(graph):
                break
            for j in range(len(graph[i])):
                if i == 0:
                    if graph[i][j] == 1:
                        path.append(j + 1)
                        i = j
                        break
                else:
                    if graph[i][j] == 1 and not((j + 1) in path):
                        path.append(j + 1)
                        i = j
                        break
        print(path)
        print(graph)

# Sample input
n = 5
m = 4
temp = [(1, 2), (2, 3), (3, 4), (4, 5)]
main(n, m, temp)
