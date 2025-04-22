def main(n):
    avg = 0
    for i in range(len(n)):
        avg += n[i]
    avg = avg/len(n)
    var = 0
    for i in range(len(n)):
        var += (n[i] - avg) ** 2
    var = var/len(n)
    
    print('Variance is: ', var)
n = [2, 3, 1, 2, 2]
main(n)
