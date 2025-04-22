from math import inf
def main(n, m, goals, temp):
    d = {}
    for i in range(m):
        if temp[i][0] not in d:
            d[temp[i][0]] = []
        d[temp[i][0]].append(temp[i][1:])
        additions = []
        for k, v in d.items():
            for j in range(len(v)):
                if v[j].count(temp[i][0]) > 0 and temp[i][1] != k:
                    additions.append([temp[i][1], int(temp[i][2]) + int(v[j][-1])])
                if v[j].count(temp[i][1]) > 0 and temp[i][0] != k:
                    additions.append([temp[i][0], int(temp[i][2]) + int(v[j][-1])])
            for j in range(len(additions)):
                v.append(additions[j])
    total_c = 0
    while len(goals) > 0:
        min_c = inf
        for v in d['English']:
            if v[0] == goals[0]:
                if int(v[1]) < min_c:
                    min_c = int(v[1])
        total_c += min_c
        goals.pop(0)
    print(total_c)
    
main(4, 5, ['Math', 'Physics', 'Chemistry', 'Biology'],
     [('English', 'Math', '10'), ('Math', 'Physics', '20'), ('English', 'Physics', '15'),
      ('Physics', 'Chemistry', '25'), ('Chemistry', 'Biology', '30')])
