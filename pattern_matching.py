def pattern_matching(a, b):
    pointer_a = 0
    pointer_b = 0
    while pointer_a < len(a) or pointer_b < len(b):
        if (pointer_a < len(a) and pointer_b < len(b)) and (a[pointer_a] == b[pointer_b] or pointer_a == "?" or pointer_b == "?"):
            pointer_a += 1
            pointer_b += 1
        elif a[pointer_a] == "*":
            if pointer_a == len(a) - 1:
                return True
            else:
                ind = pointer_a + 1
                while a[ind] == "?" or a[ind] == "*" and ind < len(a):
                    ind += 1
                if ind == len(a):
                    return True
                else:
                    while b[pointer_b] != a[ind] and pointer_b < len(b):
                        pointer_b += 1
                    if pointer_b == len(b):
                        return False
                    else:
                        pointer_a = ind
        elif b[pointer_b] == "*":
            if pointer_b == len(b) - 1:
                return True
            else:
                ind = pointer_b + 1
                while b[ind] == "?" or b[ind] == "*" and ind < len(b):
                    ind += 1
                if ind == len(b):
                    return True
                else:
                    while a[pointer_a] != b[ind] and pointer_a < len(a):
                        pointer_a += 1
                    if pointer_a == len(a):
                        return False
                    else:
                        pointer_b = ind
        else:
            return False

s = "cb"
p = "?a"
print(pattern_matching(s, p))