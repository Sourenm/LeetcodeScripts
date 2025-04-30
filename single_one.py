def single_one(arr):
    while len(arr) > 0:
        num = arr.pop(0)
        try:
            arr.pop(arr.index(num))
        except:
            return num

nums = [4, 1, 2, 1, 2]
print(single_one(nums))
