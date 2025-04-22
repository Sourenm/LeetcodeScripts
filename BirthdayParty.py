def main(c, p, temp):
    index = 0
    while True:
        flag = 0
        if c == 0 and p[index] == 0:
            break
        lst = []
        for i in range(p[index]):
            lst.append(temp[i][0])
        for i in range(len(lst)):
            temp_copy = lst.copy()
            temp_copy.pop(i)
            test = set(temp_copy)
            if len(test) != c:
                print('YES')
                flag = 1
                break
        if flag == 0:
            print('NO')

c = 4
p = [3]
temp = [(1, 2), (2, 3), (3, 4)]
main(c, p, temp)
