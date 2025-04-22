def main(n, size, temp):
    package = []
    for i in range(size):
        if temp[i] not in package:
            package.append(temp[i])
    print(len(package))
n = 5
size = 8
temp = [1, 2, 3, 2, 4, 5, 1, 3]
main(n, size, temp)
