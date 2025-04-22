def main(x, y, n, arr1, arr2):
    i = 0
    arr1 = [0 for i in range(n)]
    arr2 = [0 for i in range(n)]
    i = 0
    j = 1
    nonin = False
    nonsur = False
    nonbi = False
    temp = 0
    while i < n:
        j = i + 1
        while j < n:
            if arr1[i] == arr1[j]:
                if arr2[i] != arr2[j]:
                    temp = 1
            j += 1
        i += 1
    if temp == 0:
        nonin = True
    i = 0
    j = 1
    no_eq = 0
    if n >= (len(y) - 1):
        while i < n:
            j = 1
            while j <= (len(y) - 1):
                if arr2[i] == int(y[j]):
                    no_eq += 1
                j += 1
            i += 1
    else:
        nonsur = False
        nonbi = False
    if no_eq >= (len(y) - 1):
        nonsur = True
    if nonsur and nonin:
        nonbi = True
    if nonbi:
        print('Bijective')
    elif nonsur:
        print('Surjective')
    elif nonin:
        print('Injective')
    else:
        print('Nothing')

x_sample = 3
y_sample = [1, 2, 3, 4]
n_sample = 3
arr1_sample = [1, 2, 3]
arr2_sample = [2, 3, 4]
main(x_sample, y_sample, n_sample, arr1_sample, arr2_sample)
