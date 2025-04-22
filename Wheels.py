import math
def main(n, wheels):
    neighbors = {}
    for i in range(n):
        if i == 0:
            wheels[i].append(0)
            wheels[i].append(1)
        else:
            wheels[i].append(-1)
        if len(wheels) > 1:
            for j in range(0, i):
                if math.sqrt(((wheels[j][0] - wheels[i][0]) ** 2) + ((wheels[j][1] - wheels[i][1]) ** 2)) == (wheels[j][2] + wheels[i][2]):
                    if j not in neighbors:
                        neighbors[j] = []
                    neighbors[j].append(i)
                    if i not in neighbors:
                        neighbors[i] = []
                    neighbors[i].append(j)
                    if wheels[j][3] != -1:
                        wheels[i][3] = 1 - wheels[j][3]
                        if wheels[j][2] % wheels[i][2] == 0:
                            wheels[i].append(wheels[j][2] // wheels[i][2])
                        else:
                            div = 0
                            for x in range(1, int((min(wheels[j][2], wheels[i][2])) / 2)):
                                if wheels[j][2] % x == 0 and wheels[i][2] % x == 0:
                                    div = x
                            wheels[i].append(f'{wheels[j][2] / div}/{wheels[i][2] / div}')
    for i in range(n):
        if wheels[i][3] == 0:
            print(f'{wheels[i][4]} Clockwise')
        elif wheels[i][3] == 1:
            print(f'{wheels[i][4]} Counterclockwise')
        else:
            print('No Movement')
    

n = 3
wheels = [
    [0.0, 0.0, 1.0, -1],
    [3.0, 0.0, 2.0, -1],
    [6.0, 0.0, 1.0, -1]
]
main(n, wheels)