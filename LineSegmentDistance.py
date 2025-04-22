from math import sqrt as s
def main(n):
    first = [n[0], n[1]]
    second = [n[2], n[3]]
    third = [n[4], n[5]]
    fourth  = [n[6], n[7]]
    m1 = (second[1] - first[1]) / (second[0] - first[0])
    m2 = (fourth[1] - third[1]) / (fourth[0] - third[0])
    c1 = first[1] - m1 * first[0]
    c2 = third[1] - m2 * third[0]
    
    d1 = abs(first[1] - first[0] * m2 - c2)/s(1 + m2 ** 2)
    d2 = abs(second[1] - second[0] * m2 - c2)/s(1 + m2 ** 2)
    d3 = abs(third[1] - third[0] * m1 - c1)/s(1 + m1 ** 2)
    d4 = abs(fourth[1] - fourth[0] * m1 - c1)/s(1 + m1 ** 2)
    print(d1)
    print(d2)
    print(d3)
    print(d4)
main([1, 2, 3, 4, 5, 6, 7, 8])
