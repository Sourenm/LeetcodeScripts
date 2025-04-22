def main(n, l, m, temp):
    for i in range(n):
        moves = 0
        length = int(temp[i][0]) / 100
        position = temp[1]
        if position == 'right':
            moves += 1
        for j in range(1, m):
            if position == temp[i][1] and (int(temp[i][0]) / 100 + length) <= l:
                length += int(temp[i][0]) / 100
            elif position == temp[i][1] and (int(temp[i][0]) / 100 + length) > l:
                moves += 2
                length = int(temp[i][0]) / 100
            elif position != temp[i][1]:
                moves += 1
                position = temp[i][1]
                length = int(temp[i][0]) / 100
        print(moves + 1)
    
    

n_sample = 3
l_sample = 5
m_sample = 4
temp_sample = [
    (200, 'left'),
    (150, 'right'),
    (300, 'left'),
]
main(n_sample, l_sample, m_sample, temp_sample)
