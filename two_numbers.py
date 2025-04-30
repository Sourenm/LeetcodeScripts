def two_numbers(lst1, lst2):
    length = max(len(lst1), len(lst2))
    count = 0
    final = []
    carry_over = 0
    while count < length:
        if count < len(lst1) and count < len(lst2):
            final.append((lst1[count] + lst2[count] + carry_over) % 10)        
            carry_over = (lst1[count] + lst2[count] + carry_over) // 10
            count += 1
        elif count > len(lst1):
            for i in range(count, len(lst2)):
                final.append((lst2[count] + carry_over) % 10)
                carry_over = (lst2[count] + carry_over) // 10                    
        elif count > len(lst2):
            for i in range(count, len(lst1)):
                final.append((lst1[count] + carry_over) % 10)
                carry_over = (lst1[count] + carry_over) // 10                                    
        else:
            break
    return final

l1 = [2,4,3]
l2 = [5,6,4]

print(two_numbers(l1, l2))
