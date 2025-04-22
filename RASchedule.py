def main(n, m, temp):
    d = {}
    for i in range(n):
        d[temp[i][0]] = []
        for j in range(1, len(temp[i])):
            d[temp[i][0]].append(int(temp[i][j]))
        d[temp[i][0]].append(0)
    day_counter = 1
    max_days = 0
    assignments = []
    assignments.append([])
    while day_counter <= m:
        current_candidate = ''
        for i in d.keys():
            if day_counter in d[i][1:-1]:
                if current_candidate != '':
                    if d[i][0] < d[current_candidate][0] or d[i][-1] < d[current_candidate][-1]:
                        current_candidate = i
                else:
                    if i not in assignments[-1]:
                        current_candidate = i
        if current_candidate in d:
            assignments[-1].append(current_candidate)
            d[current_candidate][-1] += 1
            if d[current_candidate][-1] > max_days:
                max_days = d[current_candidate][-1]
        day_counter += 1
    assignments.pop(-1)
    print(max_days)
    for i in range(len(assignments)):
        print(f'Day {i + 1}: {assignments[i][0]} {assignments[i][1]}')
n = 5
m = 3
temp = [
    [1, 2, 3],
    [2, 1, 3],
    [3, 1, 2],
    [4, 2, 3],
    [5, 1, 2]
]
main(n, m, temp)
