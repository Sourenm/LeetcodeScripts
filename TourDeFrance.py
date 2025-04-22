def main(f, r, fs, rs):
    ratio = []
    for i in range(f):
        for j in range(r):
            ratio.append(rs[j]/fs[i])
    ratio.sort()
    spread = []
    for i in range(1, len(ratio)):
        spread.append(ratio[i] / ratio[i - 1])
    print(round(max(spread), 2))
f = 3
r = 4
fs = [30.0, 40.0, 50.0]
rs = [11.0, 12.0, 13.0, 14.0]
main(f, r, fs, rs)