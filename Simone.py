def main(n, k, played):
    uniques = set(sorted(played))
    nums = []
    for i in range(k + 1):
            nums.append([i, 0])
    for i in range(1, k + 1):
        if i in uniques:
            nums[i] = [i, played.count(i)]
    flag = -1
    for i in range(k + 1):
        if nums[i][1] > flag:
            flag = nums[i][1]
    missing = []
    for i in range(k + 1):
        if nums[i][1] != flag:
            missing.append(nums[i])
    missing.sort(key = lambda i: i[1])
    for i in range(1, len(missing)):
        print(missing[i][0])
main(8, 5, [2, 3, 2, 4, 5, 6, 1, 2])
