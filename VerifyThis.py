def main(n, coord,):
    coord = []
    flag = 0
    for i in range(len(coord)):
        for j in range(i + 1, len(coord)):
            if coord[i][0] == coord[j][0] or coord[i][1] == coord[j][1]:
                print('INCORRECT!')
                flag = 1
                break
            temp_x = abs(coord[i][0] - coord[j][0])
            temp_y = abs(coord[i][1] - coord[j][1])
            if temp_x == temp_y:
                print('INCORRECT!')
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        print('CORRECT')
n = 4
coord = [(1, 1), (3, 3), (2, 4), (4, 2)]
main(n, coord)
