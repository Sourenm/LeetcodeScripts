from math import factorial as f
def main(n, k, difs):
    difs.sort()
    sets = []
    sets.append(difs[-1: -(k + 1): -1])
    if n == k:
        print(1)
    else:
        no = 1
        difference = n - k
        for i in range(1, difference + 1):
            no += f(k) / (f(i) * f(k - i))
        print(no)

sample_input_n = 6
sample_input_k = 3
sample_input_diffs = [5, 7, 2, 8, 4, 1]
main(sample_input_n, sample_input_k, sample_input_diffs)
