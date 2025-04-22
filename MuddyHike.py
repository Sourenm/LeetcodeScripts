from math import inf
def main(r, c, temp):
    path = []
    depth = inf
    position = [0, 0]
    next_move = [[-1, -1] for i in range(4)]
    visited = [[0 for x in range(c)] for y in range(r)]
    for i in range(r):
        path.append(temp[i])
    j = 0
    while j < (c - 1):
        if j == 0 and visited[position[0]][position[1]] == 0:
            for i in range(r):
                if path[i][j] < depth:
                    depth = path[i][j]
                    position = [i, j]
            i = position[0]
            j = position[1]
            visited[i][j] = 1
            if i == 0:
                next_move[1] = [i + 1, j]
                next_move[2] = [i, j + 1]
            elif i == (r - 1):
                next_move[0] = [i - 1, j]
                next_move[2] = [i, j + 1]
            else:
                next_move[0] = [i - 1, j]
                next_move[1] = [i + 1, j]
                next_move[2] = [i, j + 1]
        min = inf
        for i in range(len(next_move)):
            if sum(next_move[i]) != -2:
                if path[next_move[i][0]][next_move[i][1]] < min:
                    min = path[next_move[i][0]][next_move[i][1]]
                    position = [next_move[i][0], next_move[i][1]]
        if depth < min:
            depth = min
        i = position[0]
        j = position[1]
        if j == (c - 1):
            break
        visited[i][j] = 1
        if i == 0 and j == 0:
            next_move[0] = [-1, -1]
            next_move[1] = [-1, -1]
            if visited[i + 1][j] != 1:
                next_move[2] = [i + 1, j]
            else:
                next_move[2] = [-1, -1]
            if visited[i][j + 1] != 1:
                next_move[3] = [i, j + 1]
            else:
                next_move[3] = [-1, -1]
        elif i == 0 and j != 0:
            if visited[i][j - 1] != 1:
                next_move[0] = [i, j - 1]
            else:
                next_move[0] = [-1, -1]
            if visited[i][j + 1] != 1:
                next_move[1] = [i, j + 1]
            else:
                next_move[1] = [-1, -1]
            next_move[2] = [-1, -1]
            if visited[i + 1][j] != 1:
                next_move[3] = [i + 1, j]
            else:
                next_move[3] = [-1, -1]
        elif j == 0 and i != 0:
            if visited[i - 1][j] != 1:
                next_move[0] = [i - 1, j]
            else:
                next_move[0] = [-1, -1]
            if visited[i + 1][j] != 1:
                next_move[1] = [i + 1, j]
            else:
                next_move[1] = [-1, -1]
            if visited[i][j + 1] != 1:
                next_move[2] = [i, j + 1]
            else:
                next_move[2] = [-1, -1]
            next_move[3] = [-1, -1]
        elif i == (r - 1):
            if visited[i][j + 1] != 1:
                next_move[0] = [i, j + 1]
            else:
                next_move[0] = [-1, -1]
            next_move[1] = [-1, -1]
            if visited[i - 1][j] != 1:
                next_move[2] = [i - 1, j]
            else:
                next_move[2] = [-1, -1]
            if visited[i][j - 1] != 1:
                next_move[3] = [i, j - 1]
            else:
                next_move[3] = [-1, -1]
        else:
            if visited[i][j + 1] != 1:
                next_move[0] = [i, j + 1]
            else:
                next_move[0] = [-1, -1]
            if visited[i - 1][j] != 1:
                next_move[1] = [i - 1, j]
            else:
                next_move[1] = [-1, -1]
            if visited[i + 1][j] != 1:
                next_move[2] = [i + 1, j]
            else:
                next_move[2] = [-1, -1]
            if visited[i][j - 1] != 1:
                next_move[3] = [i, j - 1]
            else:
                next_move[3] = [-1, -1]
    print(depth)
    
    
    

main(3, 3, [[1, 2, 3], [2, 1, 4], [3, 5, 6]])
