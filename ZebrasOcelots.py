def main(n, order):
    counter = 0
    while True:
        if order.count('O') == 0:
            break
        else:
            index = -1
            for i in range(n - 1, -1, -1):
                if order[i] == 'O':
                    index = i
                    order[i] = 'Z'
                    break
            for i in range(index + 1, n):
                if order[i] == 'Z':
                    order[i] = 'O'
            counter += 1
    print(counter)
n = 6
order = ['Z', 'O', 'O', 'Z', 'O', 'Z']
main(n, order)