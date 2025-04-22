def main(pat, text):
    positions = []
    for i in range(len(text)):
        if text[i] == pat[0]:
            flag = 0
            for j in range(1, len(pat)):
                if text[i + j] != pat[j]:
                    flag = 1
                    break
            if flag == 0:
                positions.append(i)
    for i in range(len(positions)):
        print(positions[i], end=' ')
    print()
main(['is', 'a'], ['This', 'is', 'a', 'sample', 'text', 'for', 'testing', 'purposes.'])
