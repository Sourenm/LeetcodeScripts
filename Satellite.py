from math import inf
from math import sqrt
def main(n, dishes):
    combs = int((n * (n + 1)) / 2)
    connections = [[0 for x in range(n)] for y in range(n)]
    nearest = [-1 for x in range(n)]
    nearest_d = [inf for x in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            dist = sqrt((dishes[i][0] - dishes[j][0]) ** 2 + (dishes[i][1] - dishes[j][1]) ** 2)
            if dishes[i][2] + dishes[j][2] == dist:
                connections[i][j] = 1
                connections[j][i] = 1
            else:
                if dist < nearest_d[i]:
                    nearest[i] = j
                    nearest_d[i] = dist
                if dist < nearest_d[j]:
                    nearest[j] = i
                    nearest_d[j] = dist
    beam = 0
    
    while min(nearest_d) != inf:
            ind = nearest_d.index(min(nearest_d))
            if connections[ind][nearest[ind]] != 1:
                connections[ind][nearest[ind]] = 1
                connections[nearest[ind]][ind] = 1
                beam += nearest_d[ind] - dishes[ind][2] - dishes[nearest[ind]][2]
            nearest_d[ind] = inf
    print(beam)

n = 5 
dishes = [
    (1.0, 1.0, 1.0),
    (2.0, 2.0, 2.0),
    (3.0, 3.0, 3.0),
    (4.0, 4.0, 4.0),
    (5.0, 5.0, 5.0)
]
main(n, dishes)