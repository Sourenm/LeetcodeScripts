def start_center(edges):
    d = {}
    for i in range(len(edges)):
        if edges[i][0] in d:
            return edges[i][0]
        else:
            d[edges[i][0]] = 1
        if edges[i][1] in d:
            return edges[i][1]
        else:
            d[edges[i][1]] = 1

edges = [[1,2],[2,3],[4,2]]
print(start_center(edges))