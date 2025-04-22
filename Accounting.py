def main(n, q, com):
    peeps = [0 for x in range(n)]
    for i in range(q):
        if com[i][0] == 'SET':
            peeps[int(com[i][1])] = int(com[i][2])
        elif com[i][0] == 'RESTART':
            peeps = [int(com[i][1]) for x in range(n)]
        elif com[i][0] == 'PRINT':
            print(peeps[int(com[i][1])])

main(4, 2, [("SET", 1, 1), ("RESTART", 2, 1)])