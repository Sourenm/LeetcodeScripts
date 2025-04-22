def main(lst):
    newword = []
    lst2 = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            newword = lst[i]
            if i != j:
                newword += lst[j]
                lst2.append(newword)
    lst = []
    for i in lst2:
        flag = 0
        for j in range(len(lst)):
            if lst[j] == i:
                flag = 1
        if flag == 0:
            lst.append(i)
    print(lst)
lst = ["a", "b", "c"]
main(lst)