def main(dx):
    dx.sort()
    x = []
    x.append(0)
    x.append(dx[len(dx) - 1])
    dx.remove(dx[len(dx) - 1])
    i = 1
    while len(dx) > 0:
        a = []
        temp = abs(x[len(x) - 1] - dx[len(dx) - 1])
        leftmostincorrect = 0
        for j in range(len(x)):
            if not (abs(temp - x[j]) in dx):
                leftmostincorrect = 1
                break
        if leftmostincorrect == 0:
            x.insert(i, temp)
        else:
            x.insert(i, dx[len(dx) - 1])
        for j in range(len(x)):
            a.append(abs(x[i] - x[j]))
        j = 0
        flag = 0
        while j < len(a):
            flag = 0
            for k in range(len(dx)):
                if a[j] == dx[k]:
                    dx.remove(dx[k])
                    a.remove(a[j])
                    flag = 1
                    break
            if flag == 0:
                j += 1
        i += 1
    x.sort()
    print(x)

dx_sample = [3, 6, 1, 9, 4, 8]
main(dx_sample)
