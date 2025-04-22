def main(no, op):
    res = []
    res.append(1)
    index = 1
    for i in range(no):
        temp = 0
        if op[i][1] == '+':
            temp =  (int(op[i][0]) + int(op[i][2])) - res[index - 1]
            res.append(temp)
            index += 1
        elif op[i][1] == '-':
            temp = res[index - 1] * (int(op[i][0]) - int(op[i][2]))
            res.append(temp)
            index += 1
        elif op[i][1] == '*':
            temp = (int(op[i][0]) * int(op[i][2])) ** 2
            res.append(temp)
            index += 1
        elif op[i][1] == '/':
            if int(op[i][0]) % 2 == 0:
                res.append(int(op[i][0]) / 2)
            else:
                res.append((int(op[i][0]) + 1) / 2)
            index += 1
    print(res)
main(1, [("1", "+", "2")])