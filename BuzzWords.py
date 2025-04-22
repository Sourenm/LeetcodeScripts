def main(word1, word2):
    check1 = ''.join(word1)
    check2 = ''.join(word2)
    words = []
    words.append(check1)
    words.append(check2)
    word_count = []
    counter_start = 0
    counter = 1
    ind = 0
    mx = 0
    while True:
        word = words[ind][counter_start:counter_start + counter]
        check = 0
        for i in range(len(words)):
            check += words[i].count(word)
        if check > mx:
            mx = check
        counter_start += 1
        if counter_start + counter > len(words[ind]):
            if len(word_count) > counter - 1:
                if mx > word_count[counter - 1]:
                    word_count[counter - 1] = mx
            else:
                word_count.append(mx)
            mx = 0
            counter_start = 0
            counter += 1
            if counter >= len(words[ind]):
                ind += 1
                counter = 1
                if ind >= len(words):
                    break
    for i in range(len(word_count)):
        if word_count[i] != 1:
            print(word_count[i])

word1 = ["apple", "banana", "orange"]
word2 = ["orange", "grape", "kiwi"]
main(word1, word2)