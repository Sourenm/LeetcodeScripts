def main(n, temp):
    ins = []
    outs = []
    for i in range(n):
        ins.append(temp[i][0])
        outs.append(temp[i][1])
    l = 0.000001
    while True:
        flag = 0
        for i in range(len(ins)):
            for j in range(i + 1, len(ins)):
                if not (abs(outs[i] - outs[j]) <= l * abs(ins[i] - ins[j])):
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 1:
            l += 0.000001
        else:
            print(l)
            break

main(3, [(1.0, 2.0), (2.0, 4.0), (3.0, 6.0)])
