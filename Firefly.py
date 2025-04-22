def main(n, h, check):
    obstacles = [0 for x in range(h)]
    for i in range(n):
        if i % 2 == 0:
            for j in range(check[i]):
                obstacles[j] += 1
        else:
            for j in range(h - 1, h - check[i] - 1 , -1):
                obstacles[j] += 1
    print(min(obstacles), ' ', obstacles.count(min(obstacles)))
n = 4
h = 5
check = [2, 3, 1, 4]
main(n, h, check)