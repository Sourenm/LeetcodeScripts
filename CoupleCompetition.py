import math
from math import inf
def main(n, blocks):
    highest = max(blocks)
    peaks = []
    temp = blocks.copy()
    count = 0
    while temp.count(highest) > 0:
        peaks.append(temp.index(highest) + count)
        count += 1
        temp.pop(temp.index(highest))
    neighbors = [-1, -1]
    for i in range(n):
        visited = [0 for x in range(n)]
        init_block = i
        steps = 0
        while peaks.count(init_block) == 0:
            if init_block < len(visited):
                visited[init_block] = 1
            if i == 0:
                neighbors[0] = -1
                if visited[i + 1] != 1:
                    if blocks[i + 1] > blocks[i]:
                        neighbors[1] = blocks[i + 1]
                    else:
                        neighbors[1] = -1
                else:
                    neighbors[1] = -1
            elif i == (len(blocks) - 1):
                if visited[i - 1] != 1:
                    if blocks[i - 1] > blocks[i]:
                        neighbors[0] = blocks[i - 1]
                    else:
                        neighbors[0] = -1
                else:
                    neighbors[0] = -1
                neighbors[1] = -1
            else:
                if visited[i - 1] != 1:
                    if blocks[i - 1] > blocks[i]:
                        neighbors[0] = blocks[i - 1]
                    else:
                        neighbors[0] = -1
                else:
                    neighbors[0] = -1
                if visited[i + 1] != 1:
                    if blocks[i + 1] > blocks[i]:
                        neighbors[1] = blocks[i + 1]
                    else:
                        neighbors[1] = -1
                else:
                    neighbors[1] = -1
            if neighbors.count(-1) > 0:
                if neighbors[0] == -1:
                    init_block += 1
                else:
                    init_block -= 1
                steps += 1
                if init_block < len(visited):
                    visited[init_block] = 1
            else:
                min = math.inf
                for j in range(len(peaks)):
                    if peaks[j] > init_block:
                        check = sum(blocks[init_block: peaks[j] + 1])
                        if (check / len(blocks[init_block: peaks[j]])) > blocks[peaks[j]] and (check / len(blocks[init_block: peaks[j]])) < blocks[peaks[j]]:
                            if len(blocks[init_block: peaks[j]]) < highest:
                                highest = len(blocks[init_block: peaks[j]])
                    else:
                        if peaks[j] < init_block:
                            check = sum(blocks[peaks[j]: init_block + 1])
                            if (check / len(blocks[peaks[j]: init_block])) > blocks[init_block] and (
                                    check / len(blocks[peaks[j]: init_block])) < blocks[peaks[j]]:
                                if len(blocks[peaks[j]: init_block]) < min:
                                    min = len(blocks[peaks[j]: init_block])
                steps += min
                break
        print(steps, end=' ')
    
    
    

n = 6
blocks = [3, 2, 6, 4, 5, 1]
main(n, blocks)
