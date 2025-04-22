from math import sqrt
def main(l, h, check):
    count = 0
    prime_count = 1
    num = 3
    if check in '2' and l >= 1:
        count += 1
    while True:
        flag = 0
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                flag = 1
                break
        if flag == 0:
            prime_count += 1
            if prime_count >= l and prime_count <= h:
                if check in str(num):
                    count += 1
            elif prime_count > h:
                break
        num += 1
    print(count)
    

l = 2
h = 20
check = '3'
main(l, h, check)
