import math
def main(n, x1, y1, x2, y2, x3, y3):
    
    for i in range(n):
        if (x1[i] - x2[i]) == 0:
            m1 = math.inf
        else:
            m1 = (y1[i] - y2[i]) / (x1[i] - x2[i])
        if (x3[i] - x1[i]) == 0:
            m2 = math.inf
        else:
            m2 = (y3[i] - y1[i]) / (x3[i] - x1[i])
        if abs(m1) == abs(m2):
            print(f'Case #{i}: not a triangle')
        else:
            d1 = math.sqrt((x1[i] - x2[i]) ** 2 + (y1[i] - y2[i]) ** 2)
            d2 = math.sqrt((x3[i] - x2[i]) ** 2 + (y3[i] - y2[i]) ** 2)
            d3 = math.sqrt((x1[i] - x3[i]) ** 2 + (y1[i] - y3[i]) ** 2)
            l = max(d1, max(d2, d3))
            if d1 == d2 or d1 == d3 or d2 == d3:
                type = 1
            elif d1 != d2 and d1 != d3 and d2 != d3:
                type = 2
            if l == d1:
                if d2 > d3:
                    m = d2
                    s = d3
                else:
                    m = d3
                    s = d2
            elif l == d2:
                if d1 > d3:
                    m = d1
                    s = d3
                else:
                    m = d3
                    s = d1
            elif l == d3:
                if d2 > d1:
                    m = d2
                    s = d1
                else:
                    m = d1
                    s = d2
            if (m + s) < l:
                print(f'Case #{i}: not a triangle')
            else:
                if l == math.sqrt((m ** 2) + (s ** 2)):
                    if type == 1:
                        print(f'Case #{i}:isosceles right triangle')
                    else:
                        print(f'Case #{i}:scalene right triangle')
                elif (l ** 2) > ((m ** 2) + (s ** 2)):
                    if type == 1:
                        print(f'Case #{i}:isosceles obtuse triangle')
                    else:
                        print(f'Case #{i}:scalene obtuse triangle')
                elif (l ** 2) < ((m ** 2) + (s ** 2)):
                    if type == 1:
                        print(f'Case #{i}:isosceles acute triangle')
                    else:
                        print(f'Case #{i}:scalene acute triangle')
main(3, [1.0, 2.0, 3.0], [1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0], [7.0, 8.0, 9.0])
