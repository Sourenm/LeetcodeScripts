def main(a, b):
    count = 0
    for i in range(a, b + 1):
        check = str(i)
        check2 = check[::-1]
        flag = 0
        p_check = 3
        while p_check <= len(check):
            for j in range(len(check)):
                if j + p_check <= len(check):
                    temp = check[j: j + p_check]
                    if temp in check2:
                        flag = 1
                        break
                else:
                    break
            if flag == 1:
                break
            else:
                p_check += 1
        if flag == 0:
            count += 1
    print(count)

main(3, 4)