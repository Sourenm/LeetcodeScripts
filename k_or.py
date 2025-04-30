def k_or(nums, k):
    bins = [list(str(bin(n)[2:])) for n in nums]
    max_len = len(bins[0])
    for num in bins:
        if len(num) > max_len:
            max_len = len(num)
    for num in bins:
        if len(num) < max_len:
            num.insert(0, '0')
    final = ''
    for j in range(max_len):
        sum = 0
        for i in range(len(bins)):
            if bins[i][j] == '1':
                sum += 1
        if sum >= k:
            final += '1'
        else:
            final += '0'
    return int(final, 2)


nums = [7,12,9,8,9,15]
print(k_or(nums, 4))

