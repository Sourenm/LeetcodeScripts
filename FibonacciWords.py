def main(n, p):
    f1 = '0'
    f2 = '1'
    count = 2
    words = 0
    while count <= n:
        temp = f1
        f1 = f2
        f2 += temp
        count += 1
    print(f2.count(p))

n_sample = 10
p_sample = '10'
main(n_sample, p_sample)
