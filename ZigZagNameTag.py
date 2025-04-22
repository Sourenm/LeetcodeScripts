import string
def main(n):
    values = {}
    for index, letter in enumerate(string.ascii_lowercase):
       values[index + 1] = letter
    length = 1
    temp = n
    while temp > 0:
        length += 1
        temp -= 25
    st = []
    st.append('a')
    while n > 0:
        if n <= 25:
            for i in range(len(st)):
                if values[n + 1] < st[i]:
                    st.insert(i, values[n + 1])
                    break
            break
        else:
            st.append('z')
            n -= 25
    print(''.join(st))
main(5)