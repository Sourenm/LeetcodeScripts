def main(n, temp):
    scores = []
    for i in range(n):
        scores.append(temp[i][0] * 10 + temp[i][1])
    sorted(scores)
    sum = []
    for i in range(n // 2):
        sum.append(scores[i] + scores[- (i + 1)])
    check = sum[0]
    flag = 0
    for i in range(1, len(sum)):
        if sum[i] != check:
            print('Impossible')
            flag = 1
            break
    if flag == 0:
        print('Possible')
n_sample = 4
temp_sample = [
    (5, 7),
    (3, 8),
    (6, 4),
    (2, 9)
]
main(n_sample, temp_sample)
