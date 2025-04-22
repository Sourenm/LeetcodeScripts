def main(st):
    i = 0
    stack = []
    while len(st) > 0:
        if st[i] == 'S' and st[i + 1] == 'S':
            end = st.index('N')
            no = ''
            if st[i + 2] == 'S':
                sign = 1
            else:
                sign = -1
            for j in range(i + 3, end):
                if st[j] == 'S':
                    no += '0'
                if st[j] == 'T':
                    no += '1'
            stack.append(int(no, 2) * sign)
            temp = st[end + 1:]
            st = temp.copy()
        elif st[i] == 'S' and st[i + 1] == 'N' and st[i + 2] == 'S':
            if len(stack) == 0:
                print('Invalid copy operation')
            else:
                temp = stack[-1]
                stack.append(temp)
            temp = st[3:]
            st = temp.copy()
        elif st[i] == 'S' and st[i + 1] == 'N' and st[i + 2] == 'T':
            if len(stack) < 2:
                print('Invalid swap operation')
            else:
                temp1 = stack[-1]
                temp2 = stack[-2]
                stack.pop()
                stack.pop()
                stack.append(temp1)
                stack.append(temp2)
            temp = st[3:]
            st = temp.copy()
        elif st[i] == 'S' and st[i + 1] == 'N' and st[i + 2] == 'N':
            if len(stack) == 0:
                print('Invalid remove operation')
            else:
                stack.pop()
            temp = st[3:]
            st = temp.copy()
        elif st[i] == 'T' and st[i + 1] == 'S' and st[i + 2] == 'S' and st[i + 3] == 'S':
            if len(stack) < 2:
                print('Invalid addition operation')
            else:
                temp1 = stack[-1]
                temp2 = stack[-2]
                stack.pop()
                stack.pop()
                stack.append(temp1 + temp2)
            temp = st[4:]
            st = temp.copy()
        elif st[i] == 'T' and st[i + 1] == 'S' and st[i + 2] == 'S' and st[i + 3] == 'T':
            if len(stack) < 2:
                print('Invalid subtraction operation')
            else:
                temp1 = stack[-1]
                temp2 = stack[-2]
                stack.pop()
                stack.pop()
                stack.append(temp1 * temp2)
            temp = st[4:]
            st = temp.copy()
        elif st[i] == 'T' and st[i + 1] == 'S' and st[i + 2] == 'S' and st[i + 3] == 'N':
            if len(stack) < 2:
                print('Invalid product operation')
            else:
                temp1 = stack[-1]
                temp2 = stack[-2]
                stack.pop()
                stack.pop()
                stack.append(temp1 * temp2)
            temp = st[4:]
            st = temp.copy()
        elif st[i] == 'T' and st[i + 1] == 'S' and st[i + 2] == 'T' and st[i + 3] == 'S':
            if len(stack) < 2:
                print('Invalid division operation')
            else:
                temp1 = stack[-1]
                temp2 = stack[-2]
                if temp1 == 0:
                    print('Division by Zero')
                else:
                    stack.pop()
                    stack.pop()
                    stack.append(temp2 // temp1)
        elif st[i] == 'T' and st[i + 1] == 'N' and st[i + 2] == 'S' and st[i + 3] == 'T':
            if len(stack) == 0:
                print('Invalid print operation')
            else:
                print(stack[-1])
                stack.pop()
            temp = st[4:]
            st = temp.copy()
instructions = ['SSNS10100TSSSSNTSN', 'TSSTSSN', 'SSNSTSN', 'TSSTSSSNTSSSNTSS']
main(instructions)
