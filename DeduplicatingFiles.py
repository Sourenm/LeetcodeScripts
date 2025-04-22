def main(n, st):
    hashes = [0 for x in range(n)]
    for i in range(n):
        check = ord(st[i][0])
        for j in range(1, len(st[i])):
            temp = ord(st[i][j])
            check = check ^ temp
        hashes[i] = check
    uniques = set(hashes)
    collisions = len(hashes) - len(uniques) + 1
    print(collisions, ' ', len(uniques))
    print(hashes)
n = 4
st = ["abc", "def", "abc", "xyz"]
main(n, st)