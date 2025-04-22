def main(n, arr):
    last = n
    first = 1
    level = 1
    while arr != sorted(arr):
        if level % 2 == 0:
            check = arr.index(last)
            print(last - (check + 1))
            arr.pop(check)
            arr.insert(last - 1, last)
            last -= 1
        else:
            check = arr.index(first)
            print(check - (first - 1))
            arr.pop(check)
            arr.insert(first - 1, first)
            first += 1
        level += 1
n = 5
arr = [4, 3, 1, 5, 2]
main(n, arr)