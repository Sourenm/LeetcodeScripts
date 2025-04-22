def main(n, lst):    
    for i in range(n):
        count = 0
        for j in range(len(lst[i]) - 1):
            if lst[i][len(lst[i]) - 1] in lst[i][j]:
                count += 1
        print(count)
n = 3
lst = [
    ["apple", "banana", "apple"],
    ["cat", "dog", "cat"],
    ["python", "java", "ruby"]
]
main(n, lst)