from random import random
def main(c):
    attempts = []
    b = bin(c)[2:]
    count = 0
    failed = 0
    while count < 5000:
        final = ''
        flag = 0
        for i in range(len(b)):
            check = random()
            if check <= 0.5:
                t = '0'
            else:
                t = '1'
            final += t
            temp = final
            temp2 = ''
            for j in range(len(temp), len(b)):
                temp2 += '0'
            temp += temp2
            d = int(temp, 2)
            if d >= c:
                failed += 1
                flag = 1
                break
        if flag == 0:
            attempts.append(failed + 1)
            failed = 0
        count += 1
    print(sum(attempts) / len(attempts))

main(10)