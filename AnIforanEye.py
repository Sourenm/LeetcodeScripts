def main(n, temp):
    abs = open('AnIforanEye.txt')
    d = {}
    words = []
    current = ''
    for row in abs:
        line = row[:-1]
        if len(line) == 1:
            d[str(line)] = []
            current = str(line)
        else:
            d[current] = list(map(str, row.split(', ')))
            correction = d[current][-1][:-1]
            d[current][-1] = correction
            words.append(d[current])
    for i in range(n):
        result_list = []
        for j in range(len(temp[i])):
            flag = 0
            t = temp[i][j].lower()
            temp[i][j] = t
            for k in d.keys():
                if temp[i][j] in d[k]:
                    result_list.append(k)
                    flag = 1
                    break
            if len(temp[i][j]) >= 2 and flag == 0:
                for x in range(len(words)):
                    for y in range(len(words[x])):
                        if words[x][y] in temp[i][j]:
                            for z in range(len(temp[i][j])):
                                if temp[i][j][z : z+len(words[x][y])] == words[x][y]:
                                    st = temp[i][j][0 : z] + list(d)[x] + temp[i][j][z + len(words[x][y]):]
                                    result_list.append(st)
                                    flag = 1
                                    break
            if flag == 0:
                result_list.append(temp[i][j])
        print(' '.join(result_list))

n = 3
temp = [
    ["apple", "orange", "pear"],
    ["cat", "dog", "elephant"],
    ["blue", "green", "red"]
]
main(n, temp)