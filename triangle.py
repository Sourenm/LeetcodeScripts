def triangle(arr):
    dp = [float('inf') for _ in range(len(arr))]
    dp[0] = arr[0][0]
    for i in range(1, len(dp)):
        for j in range(len(arr[i])):
            dp[i] = min(dp[i - 1] + arr[i][j - 1], dp[i - 1] + arr[i][j], dp[i])
    return dp[-1]

t = [[2],[3,4],[6,5,7],[4,1,8,3]]
print(triangle(t))