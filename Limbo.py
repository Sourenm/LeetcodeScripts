from math import sqrt
def main(r, c):
    r += 1
    c += 1
    i = 2 * int(sqrt(r))
    j = 2 * int(sqrt(c))
    r_remainder = r - i
    c_remainder = c - j
    
    

main(4, 3)