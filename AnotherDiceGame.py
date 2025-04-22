from random import randint
def main(n):
    counter = 0
    check = 0
    success = 0
    while counter < 1000000:
        end_criteria = 0
        check = 0
        dice = [0 for x in range(8)]
        chosen = [0 for y in range(8)]
        while check < n:
            for i in range(len(dice)):
                dice[i] = randint(1, 6)
            if 6 in dice and end_criteria != 1 and chosen[5] != 1:
                check += 6 * dice.count(6)
                end_criteria = 1
                chosen[5] = 1
                inds = []
                for i in range(len(dice)):
                    if dice[i] == 6:
                        inds.append(i)
                for i in range(len(inds) - 1, -1, -1):
                    dice.pop(inds[i])
            else:
                mx = 0
                temp_ind = 0
                for i in range(len(dice)):
                    if mx < dice[i] * dice.count(dice[i]) and chosen[dice[i] - 1] == 0:
                        mx = dice[i] * dice.count(dice[i])
                        temp_ind = dice[i] - 1
                chosen[temp_ind] = 1
                check += mx
                inds = []
                for i in range(len(dice)):
                    if dice[i] == temp_ind + 1:
                        inds.append(i)
                for i in range(len(inds) - 1, -1, -1):
                    dice.pop(inds[i])
            if sum(chosen) == len(chosen):
                if check >= n:
                    success += 1
                break
            if len(dice) == 0:
                if chosen[5] == 1:
                    if check >= n:
                        success += 1
                break
            if check >= n and chosen[5] == 1:
                success += 1
                break
        counter += 1
    print(success / counter)
    
    

n = 20
main(n)