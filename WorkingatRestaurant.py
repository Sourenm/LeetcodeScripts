def main(n, order):
    p1 = 0
    p2 = 0
    for i in range(n):
        if order[0] == 'DROP':
            p2 += int(order[1])
            print(f'DROP 2 {order[1]}')
        elif order[0] == 'TAKE':
            p1 = p2
            print(f'MOVE 2->1 {p1}')
            p2 = 0
            p1 -= int(order[1])
            print(f'TAKE 1 {order[1]}')

n = 3
order = [
    ('DROP', 5),
    ('TAKE', 2),
    ('DROP', 3),
]
main(n, order)