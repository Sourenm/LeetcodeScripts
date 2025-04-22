from itertools import combinations as c
def main(n, mat):
    triangles = []
    for i in range(n):
        if mat[i].count(1) > 1:
            pos = []
            for j in range(n):
                if mat[i][j] == 1:
                    pos.append(j)
            final = list(c(pos, 2))
            for j in range(len(final)):
                if mat[final[j][0]][final[j][1]] == 1:
                    if sorted([i, final[j][0], final[j][1]]) not in triangles:
                        triangles.append(sorted([i, final[j][0], final[j][1]]))
    print(len(triangles))
    
    

n = 4
mat = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]
main(n, mat)