def main(a):
    count = 0
    for i in range(len(a)):
        if a[i].count('-') == 0:
            count += 1
        else:
            temp = a[i].split('-')
            count += (int(temp[1]) - int(temp[0]) + 1)
    print(count)
a = ["1-5", "7-10", "15-20", "22"]
main(a)