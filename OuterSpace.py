def main(temp, state):
    dict = []
    j = 0
    while True:
        if temp[j][0] == '#':
            break
        else:
            dict.append(temp[j])
        j += 1
    j = 0
    while True:
        if state[j][0] == '#':
            break
        else:
            words = 0
            test = state[j][:-1]
            for i in range(len(test)):
                if test[i] != '1':
                    for j in range(len(dict)):
                        if test[i] == dict[j][0]:
                            flag = 0
                            for k in range(1, len(dict[j])):
                                if test[i + k] != dict[j][k]:
                                    flag = 1
                                    break
                            if flag == 0:
                                test = list(test)
                                for k in range(i, i + len(dict[j])):
                                    test[k] = '1'
                                test = ''.join(test)
                                words += 1
            print(words)
        j += 1            

# Sample Input
temp_input = [
    "cat",
    "dog",
    "bat",
    "#",
]
state_input = [
    "catastrophe",
    "batter",
    "doghouse",
    "#",
]
main(temp_input, state_input)
