def main(n):
    counter = 0
    for i in range(10 ** (n - 1), 10 ** n):
        for j in range(2, n + 1):
            flag = 0
            temp = str(i)
            check = int(temp[0:j])
            if check % j != 0:
                flag = 1
                break
        if flag == 0:
            counter += 1
    print(counter)
main(40)