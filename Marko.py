def main(n, lst1, dial):
    count = 0
    for i in range(n):
        flag = 0
        for j in range(len(lst1[i])):
            if len(lst1[i]) != len(dial):
                flag = 1
                #print('Length!')
                break
            else:
                if dial[j] == '2':
                    if lst1[i][j] != 'a' and lst1[i][j] != 'b' and lst1[i][j] != 'c':
                        flag = 1
                        break
                if dial[j] == '3':
                    if lst1[i][j] != 'd' and lst1[i][j] != 'e' and lst1[i][j] != 'f':
                        flag = 1
                        break
                if dial[j] == '4':
                    if lst1[i][j] != 'g' and lst1[i][j] != 'h' and lst1[i][j] != 'i':
                        flag = 1
                        break
                if dial[j] == '5':
                    if lst1[i][j] != 'j' and lst1[i][j] != 'k' and lst1[i][j] != 'l':
                        flag = 1
                        break
                if dial[j] == '6':
                    if lst1[i][j] != 'm' and lst1[i][j] != 'n' and lst1[i][j] != 'o':
                        flag = 1
                        break
                if dial[j] == '7':
                    if lst1[i][j] != 'p' and lst1[i][j] != 'q' and lst1[i][j] != 'r' and lst1[i][j] != 's':
                        flag = 1
                        break
                if dial[j] == '8':
                    if lst1[i][j] != 't' and lst1[i][j] != 'u' and lst1[i][j] != 'v':
                        flag = 1
                        break
                if dial[j] == '9':
                    if lst1[i][j] != 'w' and lst1[i][j] != 'x' and lst1[i][j] != 'y' and lst1[i][j] != 'z':
                        flag = 1
                        break
        if flag == 0:
            count += 1
    print(count)
n = 3
lst1 = [['abc'], ['def'], ['xyz']]
dial = '233'
result = main(n, lst1, dial)
print(result)
