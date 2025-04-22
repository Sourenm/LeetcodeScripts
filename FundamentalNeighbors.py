def main():
    data = open('FundamentalNeighbors.txt')
    for row in data:
        primary = int(row.strip())
        roots = []
        i = 2
        while i < primary + 1:
            not_prime = 0
            for j in range(2, i):
                if i % j == 0:
                    not_prime = 1
                    break
            if not_prime == 0:
                if primary % i == 0:
                    roots.append(i)
                    primary /= i
                    i = 2
                else:
                    i += 1
            else:
                i += 1
        d = {}
        for i in range(len(roots)):
            if roots[i] not in d:
                d[roots[i]] = 1
            else:
                d[roots[i]] += 1
        neighbor_d = 0
        for key, values in d.items():
            neighbor_d += values ** key
        print(neighbor_d)
    

main()