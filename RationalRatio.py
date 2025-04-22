def main(n, p):
    temp = n.split('.')[1]
    check = n.split('.')[0] + '.'
    for i in range(int(p)):
        check += temp
    print(check)
    check = float(check)
    p = 1
    q = 1
    while True:
        if abs(p / q - check) < (10 ** -6):
            print(f'{p}/{q}')
            break
        else:
            q = q + 1
        if p / q < check:
            p += 1
            q = 1

main("3.14", 3)