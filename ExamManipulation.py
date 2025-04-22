def main(n, k, answers):
    max_l = 0
    for i in range(len(answers[0])):
        check = ''
        for j in range(i, len(answers[0])):
            check += answers[0][j]
            length = len(check)
            flag = 0
            for k in range(1, len(answers)):
                if check not in answers[k]:
                    flag = 1
                    break
            if flag == 0:
                if length > max_l:
                    max_l = length
    print(max_l)
    

n_sample = 3
k_sample = 4
answers_sample = [
    ["abcd"],
    ["ab"],
    ["bc"],
    ["cd"]
]
main(n_sample, k_sample, answers_sample)
