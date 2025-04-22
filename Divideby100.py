def main(n, m):
    count = m.count('0')
    n.insert(-count, '.')
    j = ''.join(n)
    print(float(j))
n = ['1', '2', '3', '4']
m = ['000']
main(n, m)