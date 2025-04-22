from math import inf
def main(x, yl, yh):
    min_k = 0
    max_k = 0
    flag = 0
    current = x
    if x >= yl and x <= yh:
        min_k = 0
        flag = 1
    grades = []
    grades.append(x)
    ps = 0
    while current <= yh:
        current = 10 * (current) ** 0.5
        if int(current) != current:
            current = int(current) + 1
        if len(grades) == 1 and current > yh:
            print('impossible')
            ps = 1
            break
        if current >= yl and flag == 0:
            min_k = len(grades)
            flag = 1
        if current <= yh:
            if current not in grades:
                grades.append(current)
            else:
                max_k = inf
                break
        else:
            max_k = len(grades) - 1
            break
    if ps == 0:
        print(min_k, ' ', max_k)

x = 5
yl = 2
yh = 100
main(x, yl, yh)