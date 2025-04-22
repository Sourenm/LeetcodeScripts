from math import inf
def main(n, m, peeps, trees):
    closest = [-1 for i in range(n)]
    min = inf
    for i in range(n):
        min = inf
        for j in range(m):
            if abs(peeps[i] - trees[j]) < min:
                min = abs(peeps[i] - trees[j])
                closest[i] = trees[j]
    print(len(closest) - len(set(closest)))
main(5, 3, [1, 4, 7, 10, 13], [2, 5, 9])
