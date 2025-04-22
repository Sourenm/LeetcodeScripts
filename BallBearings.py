from math import pi
def main(big_d, d, s):
    i = 1
    p = 2 * pi * (big_d / 2)
    while True:
        sm = i * (d + s)
        if sm <= p:
            i += 1
        else:
            print(i - 1)
            break
big_d = 10.0
d = 2.0
s = 1.0
main(big_d, d, s)
