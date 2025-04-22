def main(n, temp):
    before = []
    after = []
    max_range = 0
    ind = 0
    for i in range(n):
        before.append(temp[i][0])
        after.append(temp[i][1])
        if after[-1] - before[-1] > max_range:
            ind = i
            max_range = after[-1] - before[-1]
    init_drives = before[ind]
    before[ind] = 0
    available_space = after[ind]
    count = 0
    while sum(before) != 0:
        for i in range(n):
            if before[i] < available_space:
                before[i] = 0
                available_space += after[i]
        count += 1
        if count > 5:
            max_range = 0
            ind = 0
            for i in range(n):
                if after[i] - before[i] > max_range:
                    ind = i
                    max_range = after[i] - before[i]
            init_drives += before[ind]
            before[ind] = 0
            available_space += after[ind]
            count = 0
    print(init_drives)

n = 3
temp = [(5, 10), (8, 15), (12, 20)]
main(n, temp)