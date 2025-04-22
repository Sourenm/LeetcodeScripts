def main(n, x):
    st = [char for char in x]
    d = {}
    for i in range(len(st)):
        if st[i] == 'I' or st[i] == 'C' or st[i] == 'P' or st[i] == 'A' or st[i] == 'S' or st[i] == 'G':
            if st[i] not in d:
                d[st[i]] = []
            d[st[i]].append([(i // n) + 1, (i % n) + 1])
    final = 0
    if 'I' not in d or 'C' not in d or 'P' not in d or 'C' not in d or 'A' not in d or 'S' not in d or 'G' not in d:
        print('NO')
    else:
        for a in d['I']:
            for b in d['C']:
                if ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) == n:
                    for c in d['P']:
                        if ((b[0] - c[0]) ** 2 + (b[1] - c[1]) ** 2) == n:
                            for e in d['C']:
                                if ((c[0] - e[0]) ** 2 + (c[1] - e[1]) ** 2) == n:
                                    for f in d['A']:
                                        if ((e[0] - f[0]) ** 2 + (e[1] - f[1]) ** 2) == n:
                                            for g in d['S']:
                                                if ((f[0] - g[0]) ** 2 + (f[1] - g[1]) ** 2) == n:
                                                    for h in d['I']:
                                                        if ((g[0] - h[0]) ** 2 + (g[1] - h[1]) ** 2) == n:
                                                            for i in d['A']:
                                                                if ((h[0] - i[0]) ** 2 + (h[1] - i[1]) ** 2) == n:
                                                                    for j in d['S']:
                                                                        if ((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) == n:
                                                                            for k in d['G']:
                                                                                if ((j[0] - k[0]) ** 2 + (
                                                                                        j[1] - k[1]) ** 2) == n:
                                                                                    print('YES')
                                                                                    final = 1
                                                                                    break
                                                                            if final == 1:
                                                                                break
                                                                    if final == 1:
                                                                        break
                                                            if final == 1:
                                                                break
                                                    if final == 1:
                                                        break
                                            if final == 1:
                                                break
                                    if final == 1:
                                        break
                            if final == 1:
                                break
                    if final == 1:
                        break
            if final == 1:
                break
        if final == 0:
            print('NO')
n_sample = 3
x_sample = "ICPCASGICPASG"
main(n_sample, x_sample)
