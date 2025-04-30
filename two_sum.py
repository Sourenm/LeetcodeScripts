def two_sum(arr, num):
    temp = 0
    for i in range(len(arr)):
        temp = num - arr[i]
        if temp in arr[i+1:]:
            return [i, i + 1 + arr[i+1:].index(temp)]

nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))