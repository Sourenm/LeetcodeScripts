from math import inf
def main(n):
    subs = []
    for i in range(len(n)):
        for j in range(i + 1, len(n) + 1):
            subs.append(n[i : j])
    period = set(n)
    count = 0
    p = []
    for i in range(len(subs)):
        if len(subs[i]) != len(n):
            if len(set(subs[i])) == len(period):
                if subs[i] not in p:
                    p.append(subs[i])
    min_l = inf
    final = []
    for i in range(len(p)):
        if len(p[i]) < min_l:
            min_l = len(p[i])
    for i in range(len(p)):
        if len(p[i]) == min_l:
            count += 1
            final.append(p[i])
    print(count)
    print(final)
main("programming")