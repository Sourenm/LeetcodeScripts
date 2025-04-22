def main(n, m, heights, temp):
    def fib(k):
        a = 1
        b = 1
        no = 2
        if k == a or k == b:
            return 0
        else:
            while True:
                temp = b
                b += a
                a = temp
                if k == b:
                    return no
                elif b > k:
                    return -1
                no += 1
    d = {}
    for i in range(m):
        if temp[i][0] not in d:
            d[temp[i][0]] = []
        if temp[i][1] not in d:
            d[temp[i][1]] = []
        d[temp[i][0]].append(temp[i][1])
        d[temp[i][1]].append(temp[i][0])
    fib_ind = []
    for i in range(len(heights)):
        fib_ind.append(fib(heights[i]))
    count = 0
    if fib_ind.count(0) > 1:
        fib_ind[fib_ind.index(0)] = 1
    while True:
        if fib_ind[count] == -1:
            fib_ind.pop(count)
            heights.pop(count)
        else:
            count += 1
        if count > len(fib_ind) - 1:
            break
    print(heights)
    print(fib_ind)
    if len(heights) == 0:
        print(0)
    elif len(heights) == 1:
        print(1)
    else:
        score = 0

n_sample = 5
m_sample = 4
heights_sample = [2, 5, 8, 3, 7]
temp_sample = [(2, 5), (5, 8), (8, 3), (3, 7)]
main(n_sample, m_sample, heights_sample, temp_sample)