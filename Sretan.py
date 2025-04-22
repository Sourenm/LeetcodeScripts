def main(n):
    if n > 2:
        digits = n - 2
        it = 2
        while digits > 0:
            digits -= 2**it
            if digits <= 0:
                break
            it += 1
        digits = n
        out = []
        out.append('4')
        for i in range(1, it):
            digits -= 2**i
            out.append('4')
        temp = str(bin(digits - 1)[2:])
        print(temp)
        if len(temp) >= 1:
            for i in range(len(temp)):
                if temp[len(temp) - (i + 1)] == '1':
                    out[len(out) - (i + 1)] = '7'
        print(' '.join(out))
    else:
        if n == 1:
            print('4')
        else:
            print('7')
main(4)
