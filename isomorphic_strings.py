def isomorphic_strings(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for i in range(len(s)):
        c1, c2 = s[i], t[i]

        if c1 in s_to_t and s_to_t[c1] != c2:
            return False
        if c2 in t_to_s and t_to_s[c2] != c1:
            return False

        s_to_t[c1] = c2
        t_to_s[c2] = c1

    return True


s = "paper"
t = "title"
print(isomorphic_strings(s, t))