from itertools import combinations
def main(test):    
    result = []
    for i in range(len(test)):
        for j in range(0, i):
            if (i - j) > 1:
                result.append(test[j:i])
    final = []
    for i in range(len(result)):
        if len(result[i]) % 2 == 0:
            flag = 0
            for x in range(int(len(result[i]) / 2)):
                for y in range(len(result[i]) - 1, int(len(result[i]) / 2) - 1, -1):
                    if result[i][x] != result[i][y]:
                        flag = 1
                        break
            if flag == 0:
                if result[i] not in final:
                    final.append(result[i])
        else:
            flag = 0
            for x in range(int(len(result[i]) / 2)):
                for y in range(len(result[i]) - 1, int(len(result[i]) / 2), -1):
                    if result[i][x] != result[i][y]:
                        flag = 1
                        break
            if flag == 0:
                if result[i] not in final:
                    final.append(result[i])
    print(final)
test = ["racecar", "level", "deified", "python", "noon"]
main(test)