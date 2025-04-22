def main(n, temp):
    d = {}
    for i in range(5):
        for j in range(1, len(temp[i]), 2):
            if j < len(temp[i]) and j + 1 < len(temp[i]):
                if temp[i][j] not in d:
                    d[temp[i][j]] = []
                if temp[i][j + 1] not in d:
                    d[temp[i][j + 1]] = []
                d[temp[i][j]].append(temp[i][j + 1])
                d[temp[i][j + 1]].append(temp[i][j])
    parties = ['A' for x in range(n)]
    own_count = [0 for y in range(n)]
    current = 1
    for current in d.keys():
        for v in d[current]:
            if current - 1 < len(parties) and v - 1 < len(parties):
                if parties[current - 1] == 'A':
                    parties[v - 1] = 'B'
                else:
                    parties[v - 1] = 'A'
    
    print(parties)

n = 4 
temp = [
    [1, 2, 2, 3, 3, 4, 4, 5, 5, 1],
    [2, 3, 3, 4, 4, 5, 5, 1, 1, 2],
    [3, 4, 4, 5, 5, 1, 1, 2, 2, 3],
    [4, 5, 5, 1, 1, 2, 2, 3, 3, 4],
    [5, 1, 1, 2, 2, 3, 3, 4, 4, 5]
]
main(n, temp)
