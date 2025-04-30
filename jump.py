def jump(arr):
    n = 0
    while n < len(arr):
        try:
            n = n + arr[n]
            if n == len(arr) - 1:
                return True
        except:
            return False 
    return False

nums = [2, 3, 1, 1, 4]
print(jump(nums))