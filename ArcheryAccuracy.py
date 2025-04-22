from random import random
def main(n, p, s):
    
    s = sorted(s)
    p = sorted(p)
    
    final_board = []
    counter = 0
    
    while counter < 10000:
        scoreboard = 0
        index = 0
        while True:
            check = random()
            if check < p[index]:
                scoreboard += 1
            else:
                scoreboard -= 1
            if abs(scoreboard) >= s[index]:
                index += 1
            if index >= n:
                break
        final_board.append(scoreboard)
        counter += 1
    count = 0
    for i in range(len(final_board)):
        if final_board[i] >= 0:
            count += 1
    
    print(count / len(final_board))
n = 5
p = [0.2, 0.4, 0.6, 0.8, 1.0]
s = [2, 3, 1, 4, 2]
main(n, p, s)