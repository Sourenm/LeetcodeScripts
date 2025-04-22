import itertools
def main(eq):
    open_p = []
    closed_p = []
    for c in range(len(eq)):
        if eq[c] == '(':
            open_p.append(c)
        if eq[c] == ')':
            closed_p.append(c)
    pairs = []
    for i in range(len(open_p)):
        temp = []
        temp.append(open_p[len(open_p) - i - 1])
        temp.append(closed_p[i])
        pairs.append(temp)
    subsets = []
    for i in range(1, len(pairs) + 1):
        temp = list(itertools.combinations(pairs, i))
        for x in temp:
            subsets.append(x)
    print(subsets)
    results = []
    for x in range(len(subsets)):
        temp = list(eq)
        for i in range(len(subsets[x])):
            op = subsets[x][i][0]
            close = subsets[x][i][1]
            temp[op] = ' '
            temp[close] = ' '
        f = ''
        for i in temp:
            if i != ' ':
                f += i
        results.append(f)
    print(results)
equation = "(a+b)*(c-d)"
main(equation)