def smallest_int(nums):
    length = max(nums)
    min_num = min(nums)
    if min_num < 0:
        length += abs(min_num)
    final = [float('inf') for _ in range(length + 1)]
    for num in nums:
        if min_num < 0:
            final[num + min_num] = 0
        else:
            final[num] = 0
    print(final)
    for i in range(len(final)):
        if final[i] != 0:
            if min_num < 0:
                return i + min_num
            else:
                return i
    return max(nums) + 1

nums = [7,8,9,11,12]
print(smallest_int(nums))
        