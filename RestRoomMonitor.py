def main(n, t, temp):
    y = []
    no = []
    for i in range(t):        
        if temp[i][1] == 'y':
            y.append(int(temp[i][0]))
        else:
            no.append(int(temp[i][0]))
    time = 0
    flag = 0
    while len(no) != 0 and len(y) != 0:
        if len(y) != 0:
            y_user = min(y)
            y.pop(y.index(min(y)))
            if y_user <= time:
                print('No')
                flag = 1
                break
        for i in range(n - 1):
            if len(no) != 0:
                n_user = min(no)
                no.pop(no.index(min(no)))
                if n_user <= time:
                    print('No')
                    flag = 1
                    break
        if flag == 1:
            break
        time += 1
    if flag == 0:
        print('Yes')
n = 3
t = 5
temp = [
    ['2', 'y'],
    ['1', 'n'],
    ['4', 'n'],
    ['3', 'y'],
    ['5', 'n'],
]
main(n, t, temp)
