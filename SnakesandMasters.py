from math import factorial as f
def main(n):
    t = n // 2
    moves = 1
    for i in range(1, t + 1):
        temp = (n - (i * 2)) + i
        moves += f(temp) / (f(i) * f(temp - i))
    print(moves)
main(5)