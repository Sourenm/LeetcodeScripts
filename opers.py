from math import gcd

def opers(nums):
    n = len(nums) // 2
    total = []
    for _ in range(n):        
        current_max = float('-inf')
        inds = []
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (_ + 1) * gcd(nums[i], nums[j]) > current_max:
                    current_max = gcd(nums[i], nums[j])
                    inds = [i, j]
        total.append(current_max)
        nums.pop(inds[1])
        nums.pop(inds[0])
    total.sort()
    final_sum = 0
    for i in range(n):
        final_sum += total[i] * (i + 1)
    return final_sum

nums = [1,2,3,4,5,6]
print(opers(nums))
