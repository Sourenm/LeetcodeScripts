def main(check):
    while True:
        if check == 0:
            break
        i = 4
        while True:
            if check % i == 3:
                print(i)
                break
            i += 1
main(3)