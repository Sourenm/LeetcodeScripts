def main(n, lines, names):
    network = 0
    social = []
    for i in range(lines):
        if names[i][0] not in social:
            network += 1
            social.append(names[i][0])
        if names[i][1] not in social:
            network += 1
            social.append(names[i][1])
        print(network)
n = 5
lines = 4
names = [('Alice', 'Bob'), ('Bob', 'Charlie'), ('David', 'Alice'), ('Eve', 'Frank')]
main(n, lines, names)
