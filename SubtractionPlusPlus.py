def main(n):
    count = 0
    for i in range(1, n + 1):
        if i == 1:
            count += 1
            if n == 1:
                print('Yes')
                break
        else:
            if n - count <= i:
                if i % 2 == 1:
                    print('Yes')
                    break
                else:
                    print('No')
                    break
            else:
                flag = 0
                for j in range(1, i + 1):
                    if n - (count + j) > (i + 1):
                        count += j
                        flag = 1
                        break
                if flag == 0:
                    if (i + 1) % 2 == 1:
                        print('Yes')
                        break
                    else:
                        print('No')
                        break
    

main(4)