def beautiful(s):
    if len(s) == 2:
        if s[0] == s[1]:
            return 0
        else:
            return 1
    else:
        return beautiful(s[:len(s)//2]) + beautiful(s[len(s)//2:])


s = "0000"
print(beautiful(s))
