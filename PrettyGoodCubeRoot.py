def main(n):
    f = n ** (1 / 3)
    print((int(f) - 1) ** 3)
    print((int(f) + 1) ** 3)
    if f - int(f) == 0:
        print(int(f))
    elif f - int(f) >= 0.5:
        print(int(f) + 1)
    else:
        print(int(f) - 1)
main(27)