def ret_sum(nums1, nums2):
    zero_count_1 = sum([1 if nums1[i] == 0 else 0 for i in range(len(nums1))])
    zero_count_1_inds = [i for i in range(len(nums1)) if nums1[i] == 0]
    zero_count_2 = sum([1 if nums2[i] == 0 else 0 for i in range(len(nums2))])
    zero_count_2_inds = [i for i in range(len(nums2)) if nums2[i] == 0]
    target = abs(sum(nums1) - sum(nums2))
    print(target)
    if target - (zero_count_1 + zero_count_2) < 0:
        return -1
    else:        
        if sum(nums1) > sum(nums2):
            target += zero_count_2
            for i in range(len(zero_count_1_inds)):
                nums1[zero_count_1_inds[i]] = 1
                target -= 1
            for i in range(len(zero_count_2_inds) - 1):
                nums2[zero_count_2_inds[i]] = 1
                target -= 1                
            nums2[zero_count_2_inds[-1]] = target
        else:
            target += zero_count_1
            for i in range(len(zero_count_2_inds)):
                nums2[zero_count_2_inds[i]] = 1
                target -= 1
                print(f"First Loop: {nums1[zero_count_2_inds[i]]}, {zero_count_2_inds[i]}, {target}")
            for i in range(len(zero_count_1_inds) - 1):
                nums1[zero_count_1_inds[i]] = 1
                target -= 1                
                print(f"Second Loop: {nums2[zero_count_1_inds[i]]}, {zero_count_1_inds[i]}, {target}")
            nums1[zero_count_1_inds[-1]] = target  
            print(nums1)                  
            print(target)
    return nums1, nums2

    

num1 = [3,2,0,1,0]
num2 = [6,5,0]
print(ret_sum(num1, num2))