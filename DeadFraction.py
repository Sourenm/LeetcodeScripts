def main(n):
    flag = 0
    for i in range(len(n)):
        if n[i] == '.':
            ind = i
            if flag == 1:
                break
            flag = 1
    st = ''.join(n[:ind])
    for i in range(15):
        st += n[ind - 1]
    check = float(st)
    print(check)
    denom = 1
    nom = 1
    threshold = 10 ** -16
    while True:
        number = nom / denom
        if number - check < threshold and number - check >= 0:
            print(f'{nom}/{denom}')
            break
        elif number - check > threshold:
            denom += 1
        else:
            nom += 1
            denom = 1
n_sample = "3.141592653589793"
main(n_sample)
