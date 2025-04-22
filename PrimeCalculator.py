import math
def main(x):
    flag = 0
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            flag = 1
            print('Not Prime!')
            break
    if flag == 0:
        print('Prime!')
main(17)