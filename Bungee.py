def main(n, mounts):
    max_height = -1
    flag = 0
    srt = sorted(mounts.copy())
    for i in range(n - 2, 0, -1):
        if flag == 2:
            break
        height = 0
        begin_index = -1
        end_index = -1
        flag = 0
        for j in range(0, i - 1):
            height = srt[i] - srt[j]
            if height > max_height:
                begin_index = mounts.index(srt[i])
                end_index = mounts.index(srt[j])
                if begin_index < end_index:
                    for x in range(begin_index, end_index):
                        if mounts[x] > srt[i]:
                            flag = 1
                            break
                else:
                    for x in range(end_index, begin_index):
                        if mounts[x] > srt[i]:
                            flag = 1
                            break
                if flag == 1:
                    break
                else:
                    max_height = height
                    print(max_height)
                    flag = 2
                    break
    

n = 7
mounts = [5, 8, 2, 10, 3, 6, 4]
main(n, mounts)
