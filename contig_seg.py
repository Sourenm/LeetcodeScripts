def contig_seg(s):
    flag = True
    i = 0
    contigs = 0
    while i < len(s):
        if s[i] == '0':
            i += 1
        else:
            j = i + 1
            while j < len(s):
                if s[j] == '1':
                    j += 1
                else:
                    break
            if j > i + 1:
                contigs += 1
                if contigs > 1:
                    flag = False
                    break
            i = j
    if contigs == 0 or contigs > 1 or flag == False:
        return False
    if contigs == 1 and flag == True:
        return True

s = '110'
print(contig_seg(s))


