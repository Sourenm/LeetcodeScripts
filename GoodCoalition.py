def main(n, parties):
    checked = [0 for x in range(n)]
    p = []
    while sum(checked) != n:
        seats = 0
        max_p = parties[checked.index(0)][1]
        ind = checked.index(0)
        for i in range(n):
            if parties[i][1] > max_p and checked[i] != 1:
                max_p = parties[i][1]
                ind = i
        seats = parties[ind][0]
        checked[ind] = 1
        p.append(parties[ind][1] / 100)
        visited = [0 for x in range(n)]
        visited[ind] = 1
        while True:
            mx = parties[visited.index(0)][1]
            next_ind = visited.index(0)
            for i in range(n):
                if parties[i][1] > mx and visited[i] != 1:
                    mx = parties[i][1]
                    next_ind = i
            visited[next_ind] = 1
            p[-1] *= (parties[next_ind][1] / 100)
            seats += parties[next_ind][0]
            if seats >= 76:
                break
    print(max(p))
n_sample = 4
parties_sample = [(10, 30), (20, 40), (15, 25), (35, 5)]
main(n_sample, parties_sample)