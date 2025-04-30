def division(a, b):
    count = 0
    while a >= b:
        a -= b
        count += 1
    return count

print(division(10, 3))