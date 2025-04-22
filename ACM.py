def main(n, minions):
    rooms = 1
    current = minions[0]
    minions.pop(0)
    while len(minions) > 0:
        temp = minions.copy()
        for i in range(len(temp)):
            if (temp[i][0] >= current[0] and temp[i][0] <= current[1]) or (temp[i][1] >= current[0] and temp[i][1] <= current[1]):
                ind = minions.index(temp[i])
                minions.pop(ind)
        if len(minions) > 0:
            current = minions[0]
            rooms += 1
    print(rooms)
n = 5
minions = [(30, 75), (0, 50), (60, 150), (80, 120), (45, 90)]
main(n, minions)
