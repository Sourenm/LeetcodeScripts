def min_rotated(nums):
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        if nums[0] > nums[1]:
            return nums[1]
        else:
            return nums[0]
    left = nums[:len(nums)//2]
    right = nums[len(nums)//2 + 1:]
    if min_rotated(left) < min_rotated(right):
        return min_rotated(left)
    else:
        return min_rotated(right)

nums = [4,5,6,7,0,1,2]
print(min_rotated(nums))
