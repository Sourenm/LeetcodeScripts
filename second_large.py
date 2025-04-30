def second_large(s):
    largest = -1
    second_largest = -1
    for i in range(len(s)):
        if s[i].isdigit():
            if int(s[i]) > largest:
                second_largest = largest
                largest = int(s[i])                
            elif int(s[i]) == largest:
                continue
            elif int(s[i]) > second_largest:
                second_largest = int(s[i])

    return second_largest

s = "abc1111"
print(second_large(s))