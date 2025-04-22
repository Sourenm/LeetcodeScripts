def main(n, cards):
    stop_index = 0
    start_index = 1
    mx = sum(cards) / len(cards)
    while stop_index < len(cards) - 1:
        if stop_index == 0:
            check = sum(cards[start_index:]) / len(cards[start_index:])
        else:
            check = (sum(cards[:stop_index]) + sum(cards[start_index:])) / (len(cards[:stop_index]) + len(cards[start_index:]))
        if check > mx:
            mx = check
        if start_index < len(cards) - 1:
            start_index += 1
        else:
            stop_index += 1
            if stop_index == len(cards) - 1:
                start_index = stop_index
            else:
                start_index = stop_index + 1
    if mx < 0:
        print(0)
    else:
        print(mx)
    

main(5, [1, 2, 3, 4, 5])
