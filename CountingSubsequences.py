from itertools import combinations as c
def main(n, l, lst):
    for i in range(n):
        count = 0
        for x in range(1, len(lst[i]) + 1):
            for j in c(lst[i], x):
                if sum(j) == 47:
                    print(j)
                    count += 1
        print(count)

n_sample = 3
l_sample = [4]
lst_sample = [
    [10, 15, 7, 5],
    [3, 20, 10, 15],
    [25, 10, 7, 5]
]
main(n_sample, l_sample, lst_sample)