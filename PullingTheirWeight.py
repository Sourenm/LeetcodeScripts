def main(n, w):    
    line = int((sum(w)) / (len(w) - 1))
    while w.count(line) > 0:
        w.pop(w.index(line))
    g1 = []
    g2 = []
    for i in range(len(w)):
        if w[i] > line:
            g2.append(w[i])
        else:
            g1.append(w[i])
    if sum(g1) == sum(g2):
        print(line)
main(5, [1, 2, 3, 4, 5])
