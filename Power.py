def main(a, b):
    i = 0
    x = 1
    if b == 0:
        a = 1
    else:
        while i < b:
            x *= a
            i += 1
    print(x)
main(2, 3)