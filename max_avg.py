def max_avg(classes1, extra1):
    def inner_func(classes, extra):
        if len(classes) == 1:
            return (classes[0][0] + extra) / (classes[0][1] + extra)
        return max((classes[0][0] + i) / (classes[0][1] + i) + inner_func(classes[1:], extra - i) for i in range(extra + 1))
    return inner_func(classes1, extra1)/len(classes1)

classes = [[2,4],[3,9],[4,5],[2,10]]
extraStudents = 4
print(max_avg(classes, extraStudents))