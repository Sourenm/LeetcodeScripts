def main(n, words):
    words = []
    max_length = 0
    for i in range(len(words)):
        check = words[i]
        for j in range(i + 1, len(words)):
            if check not in words[j] and words[j] not in check:
                mx = 0
                common = [words[i][x: y] for x in range(len(words[i])) for y in range(x + 2, len(words[i]) + 1)]
                for k in range(len(common)):
                    if common[k] in words[j]:
                        if len(common[k]) > mx:
                            mx = len(common[k])
            if mx > max_length:
                max_length = mx
    print(max_length)
    
    

n = 3
words = ["apple", "banana", "orange"]
main(n, words)