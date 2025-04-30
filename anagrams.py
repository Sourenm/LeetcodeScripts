def anagrams(arr):
    d = {}
    for word in arr:
        temp = "".join(sorted(word.lower()))
        if temp not in d:
            d[temp] = [word]
        else:
            d[temp].append(word)
    final = []
    for v in d.values():
        final.append(v)
    return final

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagrams(strs))
