def main(n, temp):
    d = {}
    for i in range(20):
        if temp[i][0] not in d:
            d[temp[i][0]] = []
        if temp[i][1] not in d:
            d[temp[i][1]] = []
        if temp[i][1] not in d[temp[i][0]]:
            d[temp[i][0]].append(temp[i][1])
        if temp[i][0] not in d[temp[i][1]]:
            d[temp[i][1]].append(temp[i][0])
    animals = [[1, 2, 3, 4] for x in range(n)]
    animals[0] = [1]
    current_animal = 1
    current_zone = 1
    while current_zone < n:
        for v in d[current_zone]:
            if current_animal in animals[v -1]:
                animals[v - 1].remove(current_animal)
        current_zone += 1
        if len(animals[current_zone - 1]) != 0:
            temp = min(animals[current_zone - 1])
            animals[current_zone - 1] = [temp]
            current_animal = temp
    print(animals)
n = 5
temp = [
    [1, 2],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 1],
    [2, 4],
    [1, 3],
    [3, 5],
    [2, 5],
    [1, 4],
    [2, 1],
    [3, 2],
    [4, 3],
    [5, 4],
    [1, 5],
    [3, 1],
    [4, 2],
    [5, 3],
    [4, 1],
]
main(n, temp)
