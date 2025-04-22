def main(q, n, d, f1_s, f2_s):
    alphabet = []
    for i in range(q):
        alphabet.append(i)
    f1 = []
    f2 = []
    finalcount = 0
    for i in range(n):
        f1.append(int(f1_s[i]))
        f2.append(int(f2_s[i]))
    for i in range(q ** n):
        p = ''
        temp = i
        number = []
        flag = 0
        while True:
            r = temp % q
            for j in range(q):
                if ((temp - q * j) >= 0 and (temp - q * j) < q):
                    number.append(temp % q)
                    number.append(j)
                    flag = 1
                    break
            if flag == 1:
                break
            number.append(r)
            temp = temp // q
        list.reverse(number)
        if len(number) < n:
            for j in range(n - len(number)):
                number.insert(0,0)
        counter = 0
        for j in range(n):
            if number[j] != f1[j]:
                counter += 1
            if number[j] != f2[j]:
                counter += 1
        if counter == d:
            finalcount += 1
    print(finalcount)
q_sample = 3
n_sample = 2
d_sample = 1
f1_sample = ["0", "1"]
f2_sample = ["1", "2"]
main(q_sample, n_sample, d_sample, f1_sample, f2_sample)