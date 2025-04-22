def main(n, l, p, tr):
    cars = {}
    mx = 0
    mx_ind = 0
    for i in range(p):
        if tr[i] // l not in cars:
            cars[tr[i] // l] = 1
            if cars[tr[i] // l] > mx_ind:
                mx_ind = cars[tr[i] // l]
        else:
            cars[tr[i] // l] += 1
            if cars[tr[i] // l] > mx_ind:
                mx_ind = cars[tr[i] // l]
        dist = abs(tr[i] % l - (l / 2))
        if dist > mx:
            mx = dist
    print(int(mx))
    print(mx_ind)

n = 3
l = 10
p = 5
tr = [2, 4, 7, 15, 18]
main(n, l, p, tr)