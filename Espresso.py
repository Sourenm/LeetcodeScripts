def main(n, s, orders):
    consume = 0
    for i in orders:
        if i == '1':
            consume += 1
        elif i == '2':
            consume += 2
        elif i == '3':
            consume += 3
        elif i == '4':
            consume += 4
        elif i == '1L':
            consume += 2
        elif i == '2L':
            consume += 3
        elif i == '3L':
            consume += 4
        elif i == '4L':
            consume += 5
    usage = consume // s
    if s % consume == 0:
        usage -= 1
    print(usage)
n = 6
s = 10
orders = ['1', '2', '3', '1L', '2L', '4L']
main(n, s, orders)