from itertools import permutations
def main(x):
    source = x
    lst1 = []
    while x > 0:
        lst1.append(x % 10)
        x = x // 10
    lst1.sort()
    lst2 = list(permutations(lst1))
    result = []
    for i in range(len(lst2)):
        counter = len(lst2[i]) -1
        result.append(0)
        for j in lst2[i]:
            result[i] += j * (10 **counter)
            counter -= 1
    flag = 0
    for i in result:
        if int(i) > source:
            flag = 1
            print('Next Biggest Number is: ', i)
            break
    if flag == 0:
        print('No Bigger Number Found')
main(3)