def rotate_image(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if i > j:
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]         
    for i in range(len(mat)):
        mat[i] = mat[i][::-1]
    return(mat)

mat = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(mat)
print(rotate_image(mat))