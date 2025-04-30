def merge_intervals(arr):
    arr = sorted(arr, key=lambda x: x[0])
    final = []
    i = 0
    j = 1
    while i < len(arr) and j < len(arr):
        element_1 = arr[i][0]
        element_2 = arr[i][1]
        while j < len(arr) and arr[j][0] <= arr[i][1]:
            element_2 = arr[j][1] if arr[j][1] > element_2 else element_2
            j += 1
        final.append([element_1, element_2])
        i = j
        j = i + 1
    if final[-1][1] != arr[-1][1]:
        final.append(arr[-1])
    return final

intervals = [[1,4],[4,5]]
print(merge_intervals(intervals))