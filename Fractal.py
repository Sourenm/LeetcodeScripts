import math
def main(r, n):
    if r == 1:
        print(math.pi * (r ** 2))
    elif r == 2:
        res = math.pi * (r ** 2) + 4 * (math.pi * ((r / 2) ** 2))
        print(res)
    else:
        n -= 2
        res = math.pi * (r ** 2) + 4 * (math.pi * ((r / 2) ** 2))
        it = 4
        while n != 0:
            res += 3 * (math.pi * ((r / it) ** 2))
            n -= 1
            it *= 2
        print(res)
main(2, 3)