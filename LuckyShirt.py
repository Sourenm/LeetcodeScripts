from random import randint
def main(n, i, k):
    final_pos = []
    count = 0
    while count < 50000:
        pos = []
        pos.append(i)
        for j in range(k):
            cycle = randint(1, n)
            if cycle >= pos[-1]:
                new_pos = randint(1, cycle)
            else:
                new_pos = pos[-1]
            pos.append(new_pos)
        final_pos.append(sum(pos) / len(pos))
        count += 1
    print(sum(final_pos) / len(final_pos))
main(10, 5, 3)