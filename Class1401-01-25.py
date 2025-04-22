def main(n, temp):
    votes = {}
    for i in range(n):
        temp[i].pop(0)
        for x in range(len(temp[i])):
            if temp[i][x] not in votes:
                votes[temp[i][x]] = 1
            else:
                votes[temp[i][x]] += 1
    max = -1
    nominee = ''
    for k,v in votes.items():
        if v > max:
            max = v
            nominee =k
    print(max, ' ', nominee)
    

n = 3
temp = [
    ["John", "Alice", "Bob", "Alice", "John"],
    ["Alice", "Bob", "Alice", "Bob", "John"],
    ["Bob", "John", "Alice", "John", "Bob"],
]
main(n, temp)