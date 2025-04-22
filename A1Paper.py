def main(n, lst):
    tape = 0
    l = 2 ** (-3 / 4)
    w = 2 ** (-5 / 4)
    need = 2 ** (n - 1)
    co = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            if need - lst[i] * (2 ** (n - (i + 2))) > 0:
                if lst[i] != 1:
                    co = lst[i] - 1
                else:
                    co = lst[i]
            else:
                for x in range(lst[i]):
                    if need - x * (2 ** (n - (i + 2))) < 0:
                        co = x - 1
                        break
            if i % 2 == 0:
                tape += co * (l / (2 ** (i / 2)))
            else:
                tape += co * (w / (2 ** ((i - 1) / 2)))
            need -= lst[i] * (2 ** (n - (i + 2)))
    if need > 0:
        print('IMPOSSIBLE')
    else:
        print(tape)
main(4, [2, 3, 1, 4])