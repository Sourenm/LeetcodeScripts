from random import randint
def main(n, k):
    counter = 0
    fail = 0
    success = 0
    stats = []
    while counter < 5000:
        boxes = []
        for i in range(n):
            check = randint(1, n)
            while check in boxes:
                check = randint(1, n)
            boxes.append(check)
        index = 0
        while True:
            check_index = index
            success_flag = 0
            for _ in range(k):
                if boxes[check_index] - 1 == index:
                    success_flag = 1
                    break
                else:
                    check_index = boxes[check_index] - 1
            if success_flag == 0:
                fail += 1
                break
            else:
                if index == len(boxes) - 1:
                    success += 1
                    break
                else:
                    index += 1
        counter += 1
        stats.append(success / (success + fail))
    print(sum(stats) / len(stats))
n_sample = 5
k_sample = 2
main(n_sample, k_sample)