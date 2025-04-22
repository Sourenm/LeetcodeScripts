def main(k, temp):
    for i in range(k):
        oct = 0
        dec = 0
        hex = 0
        check = str(temp[i][1])
        flag = 0
        for j in check:
            if int(j) >= 8:
                flag = 1
                break
        if flag == 0:
            count = 0
            for i in range(len(check) - 1, -1, -1):
                oct += int(check[i]) * (8 ** count)
                count += 1
        count = 0
        for j in range(len(check) - 1, -1, -1):
            dec += int(check[j]) * (10 ** count)
            count += 1
        count = 0
        for j in range(len(check) - 1, -1, -1):
            hex += int(check[j]) * (16 ** count)
            count += 1
        print(temp[0], ' ', oct, ' ', dec, ' ', hex)
k = 2
temp = [
    ('Number1', '137'),
    ('Number2', '42'),
]
main(k, temp)
