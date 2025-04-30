def next_permute(nums):
    for i in range(len(nums) - 1,  1, -1):
        if nums[i] > nums[i - 1]:
            nums[i], nums[i - 1] = nums[i - 1], nums[i]
            return nums
    return sorted(nums)

nums = [1, 1, 5]
print(next_permute(nums))