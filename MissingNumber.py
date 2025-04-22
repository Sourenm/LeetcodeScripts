def main(x):
    sum = 0
    total_sum= ((len(x) + 1) * (len(x) + 2)) / 2
    for i in range (len(x)):
        sum += x[i]
    print('Missing Number is: ', total_sum - sum)

main([1, 2, 3, 4])