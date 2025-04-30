def min_els(nums, limit, goal):
    reach = goal - sum(nums)
    count = 0
    while True:
        if limit >= abs(reach):
            return count + 1
        else:
            nums.append(limit if goal >= 0 else -limit)
            reach = goal - sum(nums)
            count += 1

nums = [1,-10,9,1]
limit = 100
goal = 0

print(min_els(nums, limit, goal))