from math import factorial as f
def main(n, m):
    p = (n - 2) * 5 + 7
    
    if m == 0:
        sum = 0
        for i in range(p):
            sum += f(p) / (f(p - i) * f(i))
        print(sum)
    # else:
main(4, 5)