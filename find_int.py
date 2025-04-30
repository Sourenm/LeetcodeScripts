def find_int(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target and arr[mid + 1] > target:
            return mid + 1
        if arr[mid] > target and arr[mid - 1] < target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return len(arr)
        


nums = [1,3,5,6]
target = 7
print(find_int(nums, target))

