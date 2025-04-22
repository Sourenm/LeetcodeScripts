def main(n, h, w, pixels):
    groups = []
    for i in range(n):
        on = []
        off = []
        for j in range(h):
            for k in range(len(pixels[i][-1])):
                if pixels[i][-1][k] == '*':
                    on.append([j, k])
                else:
                    off.append([j, k])
        if len(groups) == 0:
            groups.append(on)
            groups.append(off)
        else:
            max_on_ind = 0
            max_on_value = 0
            max_off_ind = 0
            max_off_value = 0
            for k in range(len(groups)):
                count = 0
                for l in range(len(groups[k])):
                    if groups[k][l] in on:
                        count += 1
                if count > max_on_value:
                    max_on_ind = k
                    max_on_value = count
                count = 0
                for l in range(len(groups[k])):
                    if groups[k][l] in off:
                        count += 1
                if count > max_off_value:
                    max_off_ind = k
                    max_off_value = count
            if len(on) < len(groups[max_on_ind]):
                pop_ind = []
                for l in range(len(groups[max_on_ind])):
                    if groups[max_on_ind][l] not in on:
                        pop_ind.append(l)
                temp = []
                for l in range(len(pop_ind)):
                    temp.append(groups[max_on_ind][pop_ind[l]])
                    groups[max_on_ind].pop(pop_ind[l])
            else:
                temp = []
                for l in range(len(on)):
                    if on[l] not in groups[max_on_ind]:
                        temp.append(on[l])
                for l in range(len(temp)):
                    on.pop(temp[l])
            groups.append(temp)
            if len(off) < len(groups[max_off_ind]):
                pop_ind = []
                for l in range(len(groups[max_off_ind])):
                    if groups[max_off_ind][l] not in off:
                        pop_ind.append(l)
                temp = []
                for l in range(len(pop_ind)):
                    temp.append(groups[max_off_ind][pop_ind[l]])
                    groups[max_off_ind].pop(pop_ind[l])
            else:
                pop_ind = []
                for l in range(len(off)):
                    if off[l] not in groups[max_off_ind]:
                        pop_ind.append(l)
                temp = []
                for l in range(len(pop_ind)):
                    temp.append(off[pop_ind[l]])
            if temp not in groups:
                groups.append(temp)
    print(len(groups))
n = 3
h = 4
w = 4
pixels = [
    [
        "..*.",
        "....",
        ".*..",
        "...."
    ],
    [
        "....",
        "....",
        "....",
        "...."
    ],
    [
        ".*..",
        "....",
        "....",
        "...."
    ]
]

main(n, h, w, pixels)