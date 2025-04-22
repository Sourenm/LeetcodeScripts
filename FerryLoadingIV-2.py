def main(n, l, m, temp, temp2):
    for i in range(n):
        left = []
        right = []
        moves = 0
        if temp[i][1] == 'right':
            moves += 1
            right.append(int(temp[i][0]) / 100)
            side = 'R'
        else:
            left.append(int(temp[i][0]) / 100)
            side = 'L'
        for j in range(1, m):
            if temp2[j][1] == 'left':
                left.append(int(temp[i][0]) / 100)
            else:
                right.append(int(temp[i][0]) / 100)
        while len(left) > 0 or len(right) > 0:
            length = 0
            counter = 0
            if side == 'R':
                if len(right) != 0:
                    for i in range(len(right)):
                        if (length + right[i]) > l:
                            counter = i
                            break
                        length += right[i]
                    if counter == 0:
                        right.pop(0)
                    else:
                        for i in range(counter):
                            right.pop(0)
                    side = 'L'
                    moves += 1
                else:
                    side = 'L'
                    moves += 1
            else:
                if len(left) != 0:
                    for i in range(len(left)):
                        if (length + left[i]) > l:
                            counter = i
                            break
                        length += left[i]
                    if counter == 0:
                        left.pop(0)
                    else:
                        for i in range(counter):
                            left.pop(0)
                    side = 'R'
                    moves += 1
                else:
                    side = 'R'
                    moves += 1
        print(moves)
n = 1
l = 100
m = 3
temp = [(200, 'right')]
temp2 = [(150, 'left'), (120, 'right'), (80, 'left')]
main(n, l, m, temp, temp2)