def main(n):
    i = 1
    b = 4
    while i <= n:
        if i % 2 == 0:
            b += 4 / (2 * i + 1)
        else:
            b -= 4 / (2 * i + 1)
        i += 1
    print(b)
main(5)