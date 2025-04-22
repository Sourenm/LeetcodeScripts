def main(n, temp, x1, x2):
    w = temp[:-1]
    b = temp[-1]    
    size_w = 0
    for i in range(len(w)):
        size_w += w[i] ** 2
    size_w = size_w ** 0.5
    d_x1 = 0
    for i in range(len(w)):
        d_x1 += x1[i] * w[i]
    d_x2 = 0
    for i in range(len(w)):
        d_x2 += x2[i] * w[i]
    d_x1 += b
    d_x2 += b
    d_x1 /= size_w
    d_x2 /= size_w
    print(d_x1)
    print(d_x2)
    

main(3, [1.0, 2.0, 3.0, 4.0], [0.5, 0.3, 0.2], [0.8, 0.2, 0.4])
