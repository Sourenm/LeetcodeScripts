def coins(arr, n):
    dp = [100 for _ in range(n + 1)]
    dp[0] = 0
    for i in range(len(dp)):
        for j in range(len(arr)):
            if i - arr[j] >= 0:
                dp[i] = min(dp[i], dp[i - arr[j]] + 1)
    return dp

coin = [1, 2, 5] 
amount = 11                
print(coins(coin, amount))
            
            