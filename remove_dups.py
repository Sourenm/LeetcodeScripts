def remove_dups(nums):
    ind = 1
    count = 1
    current = nums[0]
    while True:
        if nums[ind] == current and count >= 2:
            nums.pop(ind)
        elif nums[ind] == current and count < 2:
            count += 1
            ind += 1
        else:
            current = nums[ind]
            ind += 1
            count = 1
        if ind >= len(nums):
            break
    return nums

nums = [0,0,1,1,1,1,2,3,3]
print(remove_dups(nums))


