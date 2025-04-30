def string_swap(s1, s2):
    d_s1 = {}
    d_s2 = {}
    for i in range(len(s1)):
        if s1[i] not in d_s1:
            d_s1[s1[i]] = [i]
        else:
            d_s1[s1[i]].append(i)
    for i in range(len(s2)):
        if s2[i] not in d_s2:
            d_s2[s2[i]] = [i]
        else:
            d_s2[s2[i]].append(i)
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if s2[i] not in d_s1 or s1[i] not in d_s2:
                return False            
            for j in range(len(d_s1[s2[i]])):
                s1_temp = list(s1)
                s1_temp[i], s1_temp[d_s1[s2[i]][j]] = s1_temp[d_s1[s2[i]][j]], s1_temp[i]
                if ''.join(s1_temp) == s2:
                    return True
            for j in range(len(d_s2[s1[i]])):
                s2_temp = list(s2)
                s2_temp[i], s2_temp[d_s2[s2[i]][j]] = s2_temp[d_s2[s2[i]][j]], s2_temp[i]
                if ''.join(s2_temp) == s1:
                    return True
            return False
    return True

s1 = 'attack'
s2 = 'defend'
print(string_swap(s1, s2))


