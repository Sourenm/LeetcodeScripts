def main(n):
    max = -1
    max_no = 0
    for m in range(2, n // 9):
        counter = 0
        temp = n
        while True:
            r = temp % m
            if r == 0:
                counter += 1
                if counter >= m:
                   break
            else:
                break
            temp = temp // m
        if counter > max:
            max = counter
            max_no = m
    print(max_no)
    print(max)

main(10)