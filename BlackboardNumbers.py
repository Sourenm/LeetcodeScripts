from math import sqrt
def main(n, s):
    for x in range(n):
        bin = 0
        oct = 0
        dec = 0
        for i in range(len(s[x])):
            if str(s[x][i]).isdigit():
                if int(s[x][i]) > 1:
                    bin = 1
                if int(s[x][i]) > 8:
                    oct = 1
            else:
                bin = 1
                oct = 1
                dec = 1
        if bin == 1 and oct == 1 and dec == 1:
            num = 0
            count = 0
            for i in range(len(s[x]) - 1, -1, -1):
                if str(s[x][i]).isdigit():
                   num += int(s[x][i]) * (16 ** count)
                   count += 1
                else:
                    if s[x][i] == 'A':
                        num += 10 * (16 ** count)
                    elif s[x][i] == 'B':
                        num += 11 * (16 ** count)
                    elif s[x][i] == 'C':
                        num += 12 * (16 ** count)
                    elif s[x][i] == 'D':
                        num += 13 * (16 ** count)
                    elif s[x][i] == 'E':
                        num += 14 * (16 ** count)
                    else:
                        num += 15 * (16 ** count)
                    count += 1
                    is_prime = 1
                    for j in range(2, int(sqrt(num))):
                        if num % j == 0:
                            is_prime = 0
                            break
                    print(is_prime, '/1')
        elif bin == 1 and oct == 1:
            num_dec = 0
            num_hex = 0
            count = 0
            for i in range(len(s[x]) - 1, -1, -1):
               num_hex += int(s[x][i]) * (16 ** count)
               num_dec += int(s[x][i]) * (10 ** count)
               count += 1
            is_prime = 2
            for j in range(2, int(sqrt(num_dec))):
                if num_dec % j == 0:
                    is_prime -= 1
                    break
            for j in range(2, int(sqrt(num_hex))):
                if num_hex % j == 0:
                    is_prime -= 1
                    break
            print(is_prime, '/2')
        elif bin == 1:
            num_dec = 0
            num_hex = 0
            num_oct = 0
            count = 0
            for i in range(len(s[x]) - 1, -1, -1):
               num_hex += int(s[x][i]) * (16 ** count)
               num_dec += int(s[x][i]) * (10 ** count)
               num_oct += int(s[x][i]) * (8 ** count)
               count += 1
            is_prime = 3
            for j in range(2, int(sqrt(num_dec))):
                if num_dec % j == 0:
                    is_prime -= 1
                    break
            for j in range(2, int(sqrt(num_hex))):
                if num_hex % j == 0:
                    is_prime -= 1
                    break
            for j in range(2, int(sqrt(num_oct))):
                if num_oct % j == 0:
                    is_prime -= 1
                    break
            print(is_prime, '/3')
        else:
            num_dec = 0
            num_hex = 0
            num_oct = 0
            num_bin = 0
            count = 0
            for i in range(len(s[x]) - 1, -1, -1):
               num_hex += int(s[x][i]) * (16 ** count)
               num_dec += int(s[x][i]) * (10 ** count)
               num_oct += int(s[x][i]) * (8 ** count)
               num_bin += int(s[x][i]) * (2 ** count)
               count += 1
            is_prime = 4
            for j in range(2, int(sqrt(num_dec))):
                if num_dec % j == 0:
                    is_prime -= 1
                    break
            for j in range(2, int(sqrt(num_hex))):
                if num_hex % j == 0:
                    is_prime -= 1
                    break
            for j in range(2, int(sqrt(num_oct))):
                if num_oct % j == 0:
                    is_prime -= 1
                    break
            for j in range(2, int(sqrt(num_bin))):
                if num_bin % j == 0:
                    is_prime -= 1
                    break
            print(is_prime, '/4')

n = 3
s = [["A5F"], ["123"], ["B1101"]]
main(n, s)
