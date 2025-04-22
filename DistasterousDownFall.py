def main(n, r, k, x_0, a, b):
    buckets = [0 for y in range(n)]
    while r > 0:
        x = (a * x_0 + b) % n
        if buckets[x] < k:
            buckets[x] += 1
        else:
            flag = 0
            for i in range(x - 1, -1, -1):
                if buckets[i] < k:
                    buckets[i] += 1
                    flag = 1
                    break
            if flag == 0:
                print('OverFlow')
                break
        r -= 1
        x_0 = x
    if flag != 0:
        print(x_0)
n_sample = 8
r_sample = 12
k_sample = 2
x_0_sample = 3
a_sample = 4
b_sample = 5
main(n_sample, r_sample, k_sample, x_0_sample, a_sample, b_sample)
