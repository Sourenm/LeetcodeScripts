def main(n, s, blocks, buildings):
    flag = 0
    if sum(blocks) < sum(buildings):
        print(-1)
    else:
        temp = buildings.copy()
        result = [[] for x in range(len(buildings))]
        i = 0
        check = min(temp)
        while len(temp) > 0:
            if check in blocks:
                result[i].append(check)
                temp.pop(temp.index(sum(result[i])))
                blocks.pop(blocks.index(check))
                i += 1
                if len(temp) > 0:
                    check = min(temp)
            else:
                result[i].append(min(blocks))
                check -= min(blocks)
                blocks.pop(blocks.index(min(blocks)))
            if check < 0:
                print(-1)
                flag = 1
                break
        if flag == 0:
            for i in range(len(result)):
                print(len(result[i]), ' ', result[i])
    

n = 5
s = "3"
blocks = [1, 2, 3, 4, 5]
buildings = [5, 7, 9]
main(n, s, blocks, buildings)
