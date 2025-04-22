from random import random as r
from math import inf
def main(n, m, k, temp):    
    times = []
    probabs = []
    for i in range(m):
        times.append(temp[0])
        probabs.append(1 - temp[1])    
    expected = 0
    s = 0
    while s < 1000000:
        logs = 0
        time = 0
        while logs < 3:
            checker = r()
            if checker > max(probabs):
                logs = 0
                time += k
            else:
                ind = -1
                best_time = inf
                for i in range(len(probabs)):
                    if probabs[i] > checker:
                        if times[i] < best_time:
                            best_time = times[i]
                            ind = i
                time += best_time
                logs += 1
        expected += time
        s += 1
    print(expected / s)
    
    
    
    

n = 3
m = 4
k = 10
temp = (5.0, 0.2)
main(n, m, k, temp)
