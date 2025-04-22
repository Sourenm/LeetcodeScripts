from math import factorial as f
def main(n, lst):
    count = 0
    d = {}
    d[1] = []
    d[2] = []
    d[3] = []
    for i in range(len(lst)):
        if lst[i] == 1:
            d[1].append(i)
        elif lst[i] == 2:
            d[2].append(i)
        else:
            d[3].append(i)
    ind_1 = 0
    ind_2 = 0
    ind_3 = 0
    count = 0
    while ind_1 < len(d[1]):
        while d[2][ind_2] < d[1][ind_1]:
            ind_2 += 1
            if ind_2 == len(d[2]) - 1:
                break   
        while d[3][ind_3] < d[2][ind_2]:
            ind_3 += 1
            if ind_3 == len(d[3]) - 1:
                break      
        check = len(d[2][ind_2:])
        for i in range(1, check + 1):
            if i < check:
                while d[3][ind_3] < d[2][ind_2 + i]:
                    ind_3 += 1
            check_3 = len(d[3][ind_3:])
            count += f(check) / (f(i) * f(check - i)) * check_3
        ind_1 += 1
        ind_2 = 0
        ind_3 = 0
    print(count)
    

n_sample = 7
lst_sample = [1, 2, 3, 1, 2, 3, 1]
main(n_sample, lst_sample)
