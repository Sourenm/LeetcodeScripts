def main(commands, n, temp):
    st = []
    check = ''
    if len(temp) != 0:
        for i in range(len(temp)):
            if temp[i] != ',':
                check += temp[i]
            else:
                st.append(int(check))
                check = ''
        st.append(int(check))
    flag = 0
    for i in range(len(commands)):
        if commands[i] == 'R':
            st.reverse()
        elif commands[i] == 'D':
            if len(st) != 0:
                st.pop(0)
            else:
                print('error')
                flag = 1
                break
    if flag == 0:
        print(st)
commands = ["R", "D", "R", "D"]
n = 4
temp = "1,2,3,4"
main(commands, n, temp)