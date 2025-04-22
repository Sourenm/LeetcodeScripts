def main(R, C, a):
    matrix = []
    print("Enter the entries rowwise:")
    for i in range(R):
        matrix.append(a[i])
    print('done!')
    sum = 0
    for i in range(R):
        for j in range(C):
            sum += matrix[i][j]
    r = 0
    c = 0
    column_sum = 1
    while sum != 0 and c <= C:
        sum = 0
        while column_sum != 0:
            column_sum = 0
            for i in range(R):
                column_sum += matrix[i][c]
            if column_sum == R:
                for i in range(R):
                    matrix[i][c] -= 1
                break
            else:
                for i in range(R):
                    if matrix[i][c] == 1:
                        for j in range(C):
                            matrix[i][j] += matrix[i][j]
                for i in range(R):
                    matrix[i][c] -= 1
                for i in range(R):
                    column_sum += matrix[i][c]
                print(matrix)
            column_sum = 0
            for i in range(R):
                column_sum += matrix[i][c]
    
        c += 1
        for i in range(R):
            for j in range(C):
                sum += matrix[i][j]
    print(matrix)
main(3, 4, [[1, 1, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1]])
