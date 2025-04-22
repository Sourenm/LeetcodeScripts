import math
def main(n, a, b, x):
    def abs(n):
        if n >= 0:
            return n
        return -n
    
    def prime(x):
        for i in range(2, int(math.sqrt(x) + 1)):
            if x % i == 0:
                return 1
            return -1
    
    def fact(n):
        b = 1
        for i in range(n + 1):
            b *= i
        return b
    
    def srt(a, b):
        if a <= b:
            return a, b
        return b, a

n = 5
a = 12
b = 8
x = 10
result = main(n, a, b, x)
print(result)