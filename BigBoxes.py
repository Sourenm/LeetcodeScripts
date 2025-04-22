from math import inf

def main(n, k, weights):
    partition = int(n / k)
    boxes = []
    for i in range(k):
        if i == 0:
            start = 0
            end = partition + 1
        else:
            start = end
            end = start + partition + 1
        boxes.append(weights[start:end])
    print(boxes)
    mx = inf
    while True:
        temp_max = -1
        temp_min = inf
        ind_max = 0
        ind_min = 0
        for i in range(len(boxes)):
            if sum(boxes[i]) > temp_max:
                temp_max = sum(boxes[i])
                ind_max = i
            if sum(boxes[i]) < temp_min:
                temp_min = sum(boxes[i])
                ind_min = i
        temp = boxes[ind_max].copy()
        mx_temp = mx
        mx = sum(temp)
        if mx_temp <= mx:
            print(mx_temp)
            break
        while len(temp) > 0:
            if ind_max == len(boxes) - 1:
                if (sum(boxes[ind_max - 1]) + temp[0]) < mx:
                    boxes[ind_max - 1].append(temp[0])
                    boxes[ind_max].pop(boxes[ind_max][0])
                    temp.pop(0)
                else:
                    break
            elif ind_max == 0:
                if (sum(boxes[ind_max + 1]) + temp[-1]) < mx:
                    boxes[ind_max + 1].insert(0, temp[-1])
                    boxes[ind_max].pop(boxes[ind_max][-1])
                    temp.pop(-1)
                else:
                    break
            else:
                if (sum(boxes[ind_max + 1]) + temp[-1]) < mx and (sum(boxes[ind_max - 1]) + temp[0]) < mx:
                    boxes[ind_max + 1].insert(0, temp[-1])
                    boxes[ind_max].pop(boxes[ind_max][-1])
                    temp.pop(-1)
                    boxes[ind_max - 1].append(temp[0])
                    boxes[ind_max].pop(boxes[ind_max][0])
                    temp.pop(0)
                elif (sum(boxes[ind_max + 1]) + temp[-1]) < mx:
                    boxes[ind_max + 1].insert(0, temp[-1])
                    boxes[ind_max].pop(-1)
                    temp.pop(-1)
                elif (sum(boxes[ind_max - 1]) + temp[0]) < mx:
                    boxes[ind_max - 1].append(temp[0])
                    boxes[ind_max].pop(boxes[ind_max][0])
                    temp.pop(0)
                else:
                    break

n = 8
k = 3
weights = [4, 2, 7, 1, 8, 3, 5, 6]
main(n, k, weights)