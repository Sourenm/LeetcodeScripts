def main(n):
    counter = 2
    test = ''
    for i in range(counter):
        test += '1'
    if n % 2 != 0 and n % 5 != 0:
        while True:
            check = int(test)
            if check % n == 0:
                print(len(test))
                break
            else:
                test += '1'
main(5)