def longest_vali(s):
    open_paran = s.count(")")
    closed_paran = s.count("(")
    return min(open_paran, closed_paran) * 2

s = ""
print(longest_vali(s))

