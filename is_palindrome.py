def is_palindrome(s):
    i = 0
    i_r = len(s) - 1
    while i_r > i:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[i_r].isalnum():
            i_r -= 1
            continue
        if s[i].lower() != s[i_r].lower():
            return False
        i += 1
        i_r -= 1
    return True


s=" "
print(is_palindrome(s))
