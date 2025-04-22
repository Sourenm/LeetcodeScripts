def main(n, s):
    np = 0
    for i in range(n):
        if s[i] != s[-1 - i]:
            np = 1
            break
    if np == 0:
        print(26 ** (n / 2))
    else:
        print(2)

main(5, ["a", "b", "c", "b", "a"])
