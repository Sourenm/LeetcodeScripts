def main(x):
    min = x[0]
    max = x[0]
    i = 1
    for i in range(len(x)):
        if x[i] > max:
            max = x[i]
        if x[i] < min:
            min = x[i]
    print('Maximum is: ', max)
    print('Minimum is: ', min)
main([1, 2, 3, 4, 5])