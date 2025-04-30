def max_score(nums, k):
    current_best = 0
    for i in range(k + 1):
        for j in range(len(nums), k, -1):
            temp = min(nums[_] for _ in range(i, j)) * (j - i)
            if temp > current_best:
                current_best = temp
    return current_best

nums = [5,5,4,5,4,1,1,1]
k = 0
print(max_score(nums, k))