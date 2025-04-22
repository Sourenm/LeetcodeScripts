def main(n, g, temp):
    result = [[0, 0] for x in range(n)]
    for i in range(g):
        if temp[i][1] == 'rock':
            if temp[i][3] == 'paper':
                result[int(temp[i][0]) - 1][1] += 1
                result[int(temp[i][2]) - 1][0] += 1
                result[int(temp[i][2]) - 1][1] += 1
            elif temp[i][3] == 'scissors':
                result[int(temp[i][0]) - 1][1] += 1
                result[int(temp[i][0]) - 1][0] += 1
                result[int(temp[i][2]) - 1][1] += 1
        elif temp[i][1] == 'paper':
            if temp[i][3] == 'rock':
                result[int(temp[i][0]) - 1][1] += 1
                result[int(temp[i][0]) - 1][0] += 1
                result[int(temp[i][2]) - 1][1] += 1
            elif temp[i][3] == 'scissors':
                result[int(temp[i][0]) - 1][1] += 1
                result[int(temp[i][2]) - 1][0] += 1
                result[int(temp[i][2]) - 1][1] += 1
        elif temp[i][1] == 'scissors':
            if temp[i][3] == 'rock':
                result[int(temp[i][0]) - 1][1] += 1
                result[int(temp[i][2]) - 1][0] += 1
                result[int(temp[i][2]) - 1][1] += 1
            elif temp[i][3] == 'paper':
                result[int(temp[i][0]) - 1][1] += 1
                result[int(temp[i][0]) - 1][0] += 1
                result[int(temp[i][2]) - 1][1] += 1
    for i in range(len(result)):
        print(result[i][0] / result[i][1])

n = 3
g = 2
temp = [
    (1, 'rock', 2, 'paper'),
    (3, 'scissors', 1, 'rock'),
]
main(n, g, temp)