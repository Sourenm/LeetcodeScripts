from math import factorial as f
from math import sqrt
from math import pi
from math import e
def main(n):    
    s = sqrt(2 * pi * n) * ((n ** n) / (e ** n))    
    print(f(int(n)) / s)
main(4.0)