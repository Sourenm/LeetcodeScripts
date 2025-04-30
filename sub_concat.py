def sub_concat(s, words):
    length = len(words[0])
    split_s = [s[_: _ + length] for _ in range(0, len(s), length)]
    for i in range(len(split_s)):
        if split_s[i] not in words:
            split_s[i] = "0" * len(words[0])
    final_split_s = "".join(split_s)
    final_inds = []
    print(final_split_s)
    for i in range(0, len(final_split_s) - (len(words)*len(words[0])), len(words[0])):
        check = final_split_s[i: i + len(words)*len(words[0])]
        check = [check[_: _ + length] for _ in range(0, len(check), length)]
        if len(check) != len(set(check)):
            continue
        if final_split_s[i: i + len(words)*len(words[0])].find("0") == -1:
            final_inds.append(i)
    return final_inds


            

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]
print(sub_concat(s, words))