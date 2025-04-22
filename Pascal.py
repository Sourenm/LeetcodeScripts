def main(n):
    counter = 0
    for i in range(n - 1, 0, -1):
        counter += 1
        if n % i == 0:
            break
    print(counter)
main(3)