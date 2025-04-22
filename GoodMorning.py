def main(t, n):
    if t <= 200 and t >= 1:
        for i in range(t):
            if int(n[i]) <= 200 and int(n[i]) >= 1:
                current_digit = []
                current_digit.append(n[i][0])
                for j in range(1, len(n[i])):
                    flag = int(current_digit[-1]) % 3
                    if current_digit[-1] == '0':
                        current_digit.append('0' for x in range(len(n) - j))
                        break
                    else:
                        if int(n[i][j]) >= int(current_digit[-1]):
                            if flag != 0:
                                if int(n[i][j]) >= (int(current_digit[-1]) + 3) or (int(n[i][j]) <= (int(current_digit[-1]) + (3 - int(current_digit[-1]) % 3))):
                                    current_digit.append(n[i][j])
                                else:
                                    temp = current_digit[-1]
                                    current_digit.append(temp)
                            else:
                                if n[i][j] == '6' or n[i][j] == '9':
                                    current_digit.append(n[j])
                                elif int(n[i][j]) < 6:
                                    current_digit.append('6')
                                elif int(n[i][j]) < 9:
                                    current_digit.append('9')
                        else:
                            if int(n[i][j]) == '0':
                                if current_digit[-1] != '3' and current_digit[-1] != '6' and current_digit[-1] != '9':
                                    current_digit.append('0')
                                else:
                                    temp = current_digit[-1]
                                    current_digit.append(temp)
                            else:
                                if current_digit[-1] != '3' and current_digit[-1] != '6' and current_digit[-1] != '9':
                                    current_digit.append('0')
                                else:
                                    temp = current_digit[-1]
                                    current_digit.append(temp)
                print(''.join(current_digit))

t_sample = 2
n_sample = ['16', '239']
main(t_sample, n_sample)