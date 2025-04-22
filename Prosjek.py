def main(p):
    check = 1
    while (check * p) - int(check * p) > 0:
        check += 1
    nums = [0 for x in range(5)]
    real = check * p
    init = 5
    while real > 0:
        if real >= init:
            nums[init - 1] += 1
            real -= init
        else:
            init -= 1
    while sum(nums) < check:
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != 0:
                nums[i] -= 1
                nums[i - 1] += 1
                nums[0] += 1
                break
    print(nums)
    

main(7.0)