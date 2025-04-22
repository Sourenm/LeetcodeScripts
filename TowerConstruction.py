def main(n, bw):
    no_towers = 1
    for i in range(1, n):
        if bw[i] > bw[i - 1]:
            no_towers += 1
    print(no_towers)
main(2, [1, 2])