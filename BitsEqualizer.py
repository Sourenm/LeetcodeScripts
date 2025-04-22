def main(s, t):
    changes = 0
    if s.count('1') > t.count('1'):
        print(-1)
    elif s.count('1') == t.count('1'):
        count = 0
        for i in range(len(t)):
            if t[i] != s[i]:
                count += 1
        changes += count // 2
        print(changes)
    else:
        q_marks = []
        for i in range(len(s)):
            if s[i] == '?':
                q_marks.append(i)
        temp = q_marks.copy()
        for i in range(len(q_marks)):
            if t[q_marks[i]] == '1':
                s[q_marks[i]] = '1'
                changes += 1
                temp.pop(i)
                if s.count('1') == t.count('1'):
                    break
        if s.count('1') != t.count('1'):
            for i in range(len(temp)):
                s[temp[i]] = '1'
                changes += 1
                if s.count('1') == t.count('1'):
                    break
        if len(temp) > 0:
            for i in range(len(temp)):
                s[temp[i]] = '0'
                changes += 1
        count = 0
        for i in range(len(t)):
            if t[i] != s[i]:
                count += 1
        changes += count // 2
        print(changes)
s = ["0?1??"]
t = ["01100"]
main(s, t)