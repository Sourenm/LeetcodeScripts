def lss(s):
    start = 0
    max_s = 0    
    while len(s) - start - 1 > max_s:
        d = {}
        max_temp = 0
        for i in range(start, len(s)):
            if s[i] not in d:
                d[s[i]] = 1
                max_temp += 1
            else:
                start = i
                break
        if max_temp > max_s:
            max_s = max_temp
    return max_s

s = "pwwkew"
print(lss(s))