def decode_ways(s):
    if len(s) == 1:
        if s == "0":
            return 0
        else:
            return 1
    elif len(s) == 2:
        if int(s[1]) == 0:
            if int(s[0]) > 2:
                return 0
            else:
                return 1
        elif int(s[0]) < 3 and int(s[1]) < 7:
            return 2
        else:
            return 1
    else:
        if int(s[1]) == 0:
            return 1 + decode_ways(s[2:])
        elif int(s[0]) < 3 and int(s[1]) < 7:
            return decode_ways(s[1:]) + decode_ways(s[2:])
        else:
            return 1 + decode_ways(s[1:])

s = "226"
print(decode_ways(s))