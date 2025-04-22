def main(grids, star):
    valid = 0
    for i in range(10):
        for j in range(1, 10):
            if star[i][j] == '*' and star[i][j - 1] == '*':
                valid = 1
                print('InvalidRow')
    for i in range(1, 10):
        for j in range(10):
            if star[i][j] == '*' and star[i - 1][j] == '*':
                valid = 1
                print('InvalidCol')
    for i in range(9):
        for j in range(9):
            if star[i][j] == '*' and star[i + 1][j + 1] == '*':
                valid = 1
                print('InvalidDiag')
    if valid == 0:
        gcheck = []
        for i in range(10):
            gcheck.append(0)
        valid = 0
        for i in range(10):
            for j in range(10):
                if star[i][j] == '*':
                    gcheck[int(grids[i][j])] += 1
                    if gcheck[int(grids[i][j])] > 2:
                        print('InvalidGrid')
                        valid = 1
                        break
            if valid == 1:
                break
        if valid == 0:
            print('Valid!')
main(
    [
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 1],
        [3, 4, 5, 6, 7, 8, 9, 10, 1, 2],
        [4, 5, 6, 7, 8, 9, 10, 1, 2, 3],
        [5, 6, 7, 8, 9, 10, 1, 2, 3, 4],
        [6, 7, 8, 9, 10, 1, 2, 3, 4, 5],
        [7, 8, 9, 10, 1, 2, 3, 4, 5, 6],
        [8, 9, 10, 1, 2, 3, 4, 5, 6, 7],
        [9, 10, 1, 2, 3, 4, 5, 6, 7, 8],
        [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    ],
    [
        [' ', ' ', ' ', ' ', '*', '*', '*', '*', '*', ' '],
        [' ', ' ', '*', '*', '*', '*', '*', '*', '*', ' '],
        [' ', '*', ' ', ' ', ' ', '*', '*', '*', ' ', ' '],
        ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*'],
        [' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '*', ' ', ' ', '*', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', '*', '*', '*', '*', '*', '*', ' ', ' '],
        [' ', ' ', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ']
    ]
)