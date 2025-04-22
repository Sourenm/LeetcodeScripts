def main(n, k, safe):
    routes = len(safe)
    for i in range(1, n + 1):
        if i in safe:
            routes += n - i
            safe.pop(0)
        else:
            routes += n - safe[0] + 1
        if len(safe) == 0:
            break
    print(routes)

n = 5
k = 3
safe = [2, 4, 5]
main(n, k, safe)
