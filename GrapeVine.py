def main(n, m, d, temp, peeps):
    d_skept = {}
    for i in range(n):
        d_skept[temp[i][0]] = [int(temp[i][1]), 0]
    d_network = {}
    for i in range(m):
        if temp[i][0] not in d_network:
            d_network[temp[i][0]] = []
        if temp[i][1] not in d_network:
            d_network[temp[i][1]] = []
        d_network[temp[i][0]].append(temp[i][1])
        d_network[temp[i][1]].append(temp[i][0])
    count = 0
    while count < d:
        for i in range(len(peeps)):
            for j in range(len(d_network[peeps[i]])):
                if d_skept[d_network[peeps[i]][j]][1] < d_skept[d_network[peeps[i]][j]][0]:
                    d_skept[d_network[peeps[i]][j]][1] += 1
                else:
                    if d_network[peeps[i]][j] not in peeps:
                        peeps.append(d_network[peeps[i]][j])
        count += 1
    print(len(peeps))
n_sample = 5
m_sample = 6
d_sample = 2
temp_sample = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1), (2, 4)]
peeps_sample = [1]
main(n_sample, m_sample, d_sample, temp_sample, peeps_sample)