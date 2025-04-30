def water(heights):
    amount = 0
    i = 1
    j = 2
    while i < len(heights) and j < len(heights):
        while j < len(heights) and heights[i] > heights[j]:
            j += 1
        if j == len(heights):
            j -= 2 # this is wrong
            if j > i + 1:
                for t in range(i + 1, j):
                    amount += min(heights[j], heights[i]) - heights[t] if min(heights[j], heights[i]) > heights[t] else 0
            break
        elif j > i + 1:
            for t in range(i + 1, j):
                amount += min(heights[j], heights[i]) - heights[t] if min(heights[j], heights[i]) > heights[t] else 0
            i = j
            j = i + 1
        else:
            i += 1
            j = i + 1
    return amount

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(water(height))
            
        