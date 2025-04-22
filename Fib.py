def main(n):
    a = 1
    b = 1
    i = 0
    while i < n:
        x = b
        b += a
        a = x
        print('Next number in series is: ', b)
        i += 1

main(4)