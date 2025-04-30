def all_subsets(nums):
    size = 0
    final = []
    while size < len(nums):
        if size == 0:
            final.append([])
            size += 1
        elif size == 1:
            for i in range(len(nums)):
                final.append([nums[i]])
            size += 1
        else:
            for i in range(0, len(nums), size - 1):                
                for j in range(i + 1, len(nums)):
                    temp = nums[i: i + size - 1]
                    temp.append(nums[j])
                    final.append(temp)
            size += 1
    final.append(nums)
    return final

nums = [1, 2, 3, 4]
print(all_subsets(nums))