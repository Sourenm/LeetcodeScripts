def interleaving_strings(s1, s2, s3):
    s1_ind = 0
    s2_ind = 0
    flag = 1
    for i in range(len(s3)):
        if s1_ind < len(s1) and s2_ind < len(s2):
            if flag == 1:
                if s3[i] == s1[s1_ind]:
                    print(f"S3[{i}] = S1[{s1_ind}] = {s3[i]} at i = {i}, s1_ind = {s1_ind}")
                    s1_ind += 1
                    flag = 1
                elif s3[i] == s2[s2_ind]:
                    s2_ind += 1
                    flag = 2
                else:
                    return False
            elif flag == 2:
                if s3[i] == s2[s2_ind]:
                    s2_ind += 1
                    flag = 2                
                elif s3[i] == s1[s1_ind]:
                    s1_ind += 1
                    flag = 1
                else:
                    return False                
        elif s1_ind < len(s1):
            if s3[i] == s1[s1_ind]:
                s1_ind += 1
            else:
                return False            
        elif s2_ind < len(s2):
            if s3[i] == s2[s2_ind]:
                s2_ind += 1
            else:
                return False                            
        else:            
            return False
    if s1_ind == len(s1) and s2_ind == len(s2):
        return True
    else:
        return False

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbbaccc"
print(interleaving_strings(s1, s2, s3))