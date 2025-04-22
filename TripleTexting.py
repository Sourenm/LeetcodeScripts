def main(word):
    wordlen = int(len(word)/3)
    if word[0:wordlen] != word[wordlen:2 * wordlen]:
        print(word[2* wordlen:len(word)])
    else:
        print(word[0:wordlen])

main("hello")