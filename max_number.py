def max_number(coins):
    coins.sort()
    current = 1
    for i in range(len(coins)):
        if coins[i] == 1:
            current += 1        
        elif coins[i] == current or coins[i] == i + 1:
            current += coins[i]
        else:
            break

    return current

coins = [1, 3]
print(max_number(coins))
        