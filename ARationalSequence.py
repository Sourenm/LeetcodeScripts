def main(p, q):
    if p == 1 and q == 1:
        print('1/2')
    elif p == 1:
        print(f'{q}/{q - p}')
    elif q == 1:
        print(f'1/{p + q}')
    else:
        if p > q:
            print(f'{q}/{p}')
        else:
            print(f'{q} / {q - p}')

main(4, 2)