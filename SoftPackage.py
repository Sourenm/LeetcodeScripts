def main(s, p):
    if s == p[:-1]:
        if p[-1].isdigit():
            print('Yes')
        else:
            print('No')
    elif p == s[:-1]:
        if s[-1].isdigit():
            print('Yes')
        else:
            print('No')
    else:
        t = ''
        for i in s:
            t += i.swapcase()
        if t == p:
            print('Yes')
        else:
            print('No')

main("Hello123", "Hello1234")
