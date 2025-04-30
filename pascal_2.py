def pascal(n):
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1,1]]
    s = [[1], [1,1]]
    for i in range(2, n):
        temp = [1]
        for j in range(1, len(s[-1])):
            temp.append(s[-1][j - 1] + s[-1][j])
        temp.append(1)
        s.append(temp)
        
    return s[-1]

n = 5
print(pascal(n))