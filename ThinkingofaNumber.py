from math import inf
def main(clues, temp):    
    upperbound = inf
    lowerbound = 0
    divisible = []
    
    for i in range(clues):
        if temp[i][0] == 'less':
            if int(temp[i][-1]) < upperbound:
                upperbound = int(temp[i][-1])
        elif temp[i][0] == 'greater':
            if int(temp[i][-1]) > lowerbound:
                lowerbound = int(temp[i][-1])
        elif temp[i][0] == 'divisible':
            divisible.append(int(temp[i][-1]))
    
    if upperbound == inf:
        print('INFINITE')
    else:
        outcome = []
        for i in range(lowerbound + 1, upperbound):
            flag = 0
            for j in range(len(divisible)):
                if i % divisible[j] == 0:
                    flag = 0
                else:
                    flag = 1
                    break
            if flag == 0:
                outcome.append(i)
                print(i, end=' ')
        print()
        if len(outcome) == 0:
            print('None')
    
    
    

clues = 4
temp = [
    ('less', 100),
    ('greater', 10),
    ('divisible', 3),
    ('divisible', 5),
]
main(clues, temp)