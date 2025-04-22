from math import sqrt
def main(n):
    div = []
    flag = 0
    result = []
    if n == 0:
        print(10)
    elif n == 1:
        print(11)
    else:
        check = 1
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                div.append(i)
                check *= i
        if check > n:
            div2 = []
            for i in range(len(div)):
                if div[i] >= 10:
                    temp = 1
                    while div[i] // 10 > 0:
                        temp *= div[i] // 10
                        div[i] = div[i] % 10
                    temp *= div[i] % 10
                    div[i] = temp
            for i in range(len(div)):
                if div.count(div[i]) > 1 and div[i] not in div2:
                    div2.append(div[i])
            temp_result = []
            check = n
            while len(div2) > 0:
                if check % max(div2) == 0:
                    temp_result.append(max(div2))
                    check = check / max(div2)
                else:
                    div2.pop(div2.index(max(div2)))
            while len(temp_result) > 0:
                result.append(min(temp_result))
                temp_result.pop(temp_result.index(min(temp_result)))
        else:
            if n != check and n / check >= 10:
                div = []
            elif n != check and len(div) > 0:
                div.append(int(n / check))
            print(div)
            if len(div) <= 1:
                flag = 1
                print('Impossible')
            elif len(div) == 2:
                print(f'{min(div)}{max(div)}')
            elif len(div) == 3 and div[2] * div[1] < 10:
                print(f'{min(div)}{div[2] * div[1]}')
            else:
                div.pop(div.index(1))
                result = []
                result.append(min(div))
                div.pop(div.index(min(div)))
                while len(div) > 0:
                    temp = 1
                    while len(div) > 0:
                        if temp * min(div) >= 10:
                            break
                        temp *= min(div)
                        div.pop(div.index(min(div)))
                    result.append(temp)
        if flag == 0:
            for i in range(len(result)):
                print(result[i],end='')
            print()

main(3)