def jump_game(nums):
    if len(nums) == 1:
        return 0
    if nums[0] != 0:
        return min((jump_game(nums[i:]) + 1) for i in range(1, nums[0] + 1))
    else:
        return float('inf')

nums = [2,3,0,1,4]
print(jump_game(nums))
