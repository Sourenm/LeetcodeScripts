from math import inf
def main(n):
    smallest = inf
    digits = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    if n in digits:
        if n != 6:
            smallest = digits.index(n)
        else:
            smallest = 6
        print(smallest, end=' ')
    else:
        temp = digits.copy()
        smallest = []
        check = n
        while max(temp) != -1 or check > 0:
            if check - max(temp) >= 2:
                check -= max(temp)
                smallest.append(temp.index(max(temp)))
            else:
                if check in digits:
                    if check != 6:
                        smallest.append(digits.index(check))
                        break
                    else:
                        smallest.append(6)
                        break
                else:
                    temp[temp.index(max(temp))] = -1
        temp = sorted(smallest)
        if temp[0] == 0:
            c = temp[0]
            temp[0] = temp[1]
            temp[1] = c
        for i in range(len(temp)):
            print(temp[i], end='')
        print()
    largest = []
    check_large = n
    temp = digits.copy()
    while min(temp) != inf or check_large > 0:
        if check_large - 2 >= 2:
            largest.append(1)
            check_large -= min(temp)
        else:
            if check_large - 2 == 0:
                largest.append(1)
                break
            elif check_large - 2 == 1:
                largest.append(7)
                break
    temp = sorted(largest, reverse= True)
    for i in range(len(temp)):
        print(temp[i], end='')
    print()
main(8)