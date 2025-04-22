def main(eq):
    numbers = []
    numbers.append(eq[0])
    numbers.append(eq[2])
    numbers.append(eq[4])
    per1 = []
    per2 = []
    per3 = []
    flag = 0
    for i in range(0, len(numbers[0])):
        per1.append(int(numbers[0][i : len(numbers[0])]))
    for i in range(0, len(numbers[1])):
        per2.append(int(numbers[1][i : len(numbers[1])]))
    for i in range(0, len(numbers[2])):
        per3.append(int(numbers[2][i : len(numbers[2])]))
    per1.pop(0)
    per2.pop(0)
    per3.pop(0)
    for i in range(len(per1)):
        if flag == -1:
            break
        for j in range(len(per2)):
            if eq[1] == '+':
                num1 = (int(numbers[0]) - per1[i]) / (10 ** len(str(per1[i])))
                num2 = (int(numbers[1]) - per2[j]) / (10 ** len(str(per2[j])))
                x = num2 * (10 ** len(str(per1[i]))) + per1[i]
                y = num1 * (10 ** len(str(per2[j]))) + per2[j]
                if x + y == int(numbers[2]):
                    print(int(x), ' + ', int(y), ' = ', numbers[2])
                    flag = -1
                    break
            if eq[1] == '*':
                num1 = (int(numbers[0]) - per1[i]) / (10 ** len(str(per1[i])))
                num2 = (int(numbers[1]) - per2[j]) / (10 ** len(str(per2[j])))
                x = num2 * (10 ** len(str(per1[i]))) + per1[i]
                y = num1 * (10 ** len(str(per2[j]))) + per2[j]
                if x * y == int(numbers[2]):
                    print(int(x), ' * ', int(y), ' = ', numbers[2])
                    flag = -1
                    break
    for i in range(len(per1)):
        if flag == -1:
            break
        for j in range(len(per3)):
            if eq[1] == '+':
                num1 = (int(numbers[0]) - per1[i]) / (10 ** len(str(per1[i])))
                num2 = (int(numbers[2]) - per3[j]) / (10 ** len(str(per3[j])))
                x = num2 * (10 ** len(str(per1[i]))) + per1[i]
                z = num1 * (10 ** len(str(per3[j]))) + per3[j]
                if x + int(numbers[1]) == z:
                    print(int(x), ' + ', numbers[1], ' = ', int(z))
                    flag = -1
                    break
            if eq[1] == '*':
                num1 = (int(numbers[0]) - per1[i]) / (10 ** len(str(per1[i])))
                num2 = (int(numbers[2]) - per3[j]) / (10 ** len(str(per3[j])))
                x = num2 * (10 ** len(str(per1[i]))) + per1[i]
                z = num1 * (10 ** len(str(per3[j]))) + per3[j]
                if x * int(numbers[1]) == z:
                    print(int(x), ' * ', numbers[1], ' = ', int(z))
                    flag = -1
                    break
    for i in range(len(per2)):
        if flag == -1:
            break
        for j in range(len(per3)):
            if eq[1] == '+':
                num1 = (int(numbers[1]) - per2[i]) / (10 ** len(str(per2[i])))
                num2 = (int(numbers[2]) - per3[j]) / (10 ** len(str(per3[j])))
                y = num2 * (10 ** len(str(per2[i]))) + per2[i]
                z = num1 * (10 ** len(str(per3[j]))) + per3[j]
                if int(numbers[0]) + y == z:
                    print(numbers[0], ' + ', int(y), ' = ', int(z))
                    flag = -1
                    break
            if eq[1] == '*':
                num1 = (int(numbers[1]) - per2[i]) / (10 ** len(str(per2[i])))
                num2 = (int(numbers[2]) - per3[j]) / (10 ** len(str(per3[j])))
                y = num2 * (10 ** len(str(per2[i]))) + per2[i]
                z = num1 * (10 ** len(str(per3[j]))) + per3[j]
                if int(numbers[0]) * y == z:
                    print(numbers[0], ' * ', int(y), ' = ', int(z))
                    flag = -1
                    break
eq = ["4", "*", "5", "=", "20"]
main(eq)