def main(n, land):
    colors = ['Blue', 'Orange', 'Pink', 'Green', 'Red', 'Yellow']
    pos = 0
    moves = 0
    while (pos + 1) != len(land):
        max_ind = 0
        for i in range(len(colors)):
            if land.count(colors[i]) > 0:
                if land.index(colors[i]) > max_ind:
                    max_ind = land.index(colors[i])
        for i in range(max_ind + 1):
            land[i] = 'Black'
        moves += 1
        pos = max_ind
    print(moves)
n = 7
land = ['Blue', 'Orange', 'Pink', 'Green', 'Red', 'Yellow', 'Green']
main(n, land)
