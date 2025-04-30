def validate_sudoku(arr):
    d_row = {}
    d_col = {}
    d_squares = {}
    for i in range(len(arr)):
        d_row[i] = []
        for j in range(len(arr[0])):
            if arr[i][j].isdigit():                
                d_row[i].append(arr[i][j])
                if j not in d_col:
                    d_col[j] = []            
                d_col[j].append(arr[i][j])
                if ((i//3) * 3) + j//3 not in d_squares:
                    d_squares[((i//3) * 3) + j//3] = []                                    
                d_squares[((i//3) * 3) + j//3].append(arr[i][j])
    for k, v in d_row.items():
        if len(v) != len(set(v)):
            return False
    for k, v in d_col.items():
        if len(v) != len(set(v)):
            return False
    for k, v in d_squares.items():
        if len(v) != len(set(v)):
            return False
    return True

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(validate_sudoku(board))