from math import factorial as f

def dis_subs(s, t):
    d_s = {}
    for i in range(len(s)):
        if s[i] not in d_s:
            d_s[s[i]] = 1
        else:
            d_s[s[i]] += 1
    d_t = {}
    for i in range(len(t)):
        if t[i] not in d_s:
            return 0        
        if t[i] not in d_t:
            d_t[t[i]] = 1
        else:
            d_t[t[i]] += 1
    running_sum = 0
    for k, v in d_t.items():
        if v > d_s[k]:
            return 0
        if v == d_s[k]:
            continue
        running_sum += f(d_s[k])/ f(v) * f(d_s[k] - v)
    return running_sum

s = "babgbag"
t = "bag"
print(dis_subs(s, t))

