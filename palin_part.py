def palin_part(s):
    final = []
    def inner_func(t):
        if len(t) == 1:
            final.append(t)
        elif len(t) == 2:
            if t[0] == t[1]:
                final.append(t)
            final.append(t[1])
            final.append(t[0])
        else:
            flag = True
            for i in range(len(t)):
                if i <= len(t) - i - 1:
                    if t[i] != t[len(t) - i - 1]:
                        flag = False
                        break
                else:
                    break
            final.append(t[0])
            if flag:                
                final.append(t)
            inner_func(t[1:])
            flag = True
            for i in range(len(t) - 1, -1, -1):
                if i <= len(t) - i - 1:
                    if t[i] != t[len(t) - i - 1]:
                        flag = False
                        break
                else:
                    break
            final.append(t[-1])
            if flag:
                final.append(t)
            inner_func(t[:-1])            
    inner_func(s)
    return set(final)

s = "aab"
print(palin_part(s))
            

