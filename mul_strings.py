def mul_strings(num1, num2):
    intermed = []
    for i in range(len(num1) - 1, -1, -1):
        carry_over = 0
        power = len(num1) - 1 - i
        result = 0
        for j in range(len(num2) - 1, -1, -1):
            result = ((int(num1[i]) * int(num2[j]) + carry_over) % 10) * (10 ** power) + result
            carry_over = (int(num1[i]) * int(num2[j]) + carry_over) // 10
            power += 1
        intermed.append(int(str(carry_over) + str(result)) if carry_over != 0 else result)
    return sum(intermed)


num1 = "123"
num2 = "456"
print(mul_strings(num1, num2))