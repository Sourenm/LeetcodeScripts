import math
def main(n):
    max = -1 * math.inf
    
    for i in range(len(n)):
        if n[i] > max:
            max = n[i]
    print('Maximum Number is: ', max)
main([1.0, 2.0, 3.0, 4.0])