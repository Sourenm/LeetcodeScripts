import math
def main(x, y):
    area = (250 * 250) / 2
    a = 0
    final = []
    base = 0
    seg_x = 0
    seg_y = 0
    if x == 0 and y == 0:
        print('125.00 125.00')
    else:
        if x == 0:
            a = math.sqrt(((250 - y) ** 2) / 2)
            base = 2 * (area / 2) - a
            seg_x = math.sin(math.pi / 4) * math.sqrt(2 * (250 ** 2))
            final.append(seg_x)
            seg_y = math.cos(math.pi / 4) * math.sqrt(2 * (250 ** 2))
            final.append(250 - seg_y)
        elif y == 0:
            a = math.sqrt(((250 - x) ** 2) / 2)
            base = 2 * (area / 2) - a
            seg_x = math.cos(math.pi / 4) * math.sqrt(2 * (250 ** 2))
            final.append(250 - seg_x)
            seg_y = math.sin(math.pi / 4) * math.sqrt(2 * (250 ** 2))
            final.append(seg_y)
        else:
            if x > 125:
                base = math.sqrt((250 - y) ** 2 + x ** 2)
                a = 2 * (area / 2) - base
                final.append(0)
                final.append(250 - a)
            else:
                base = math.sqrt((250 - x) ** 2 + y ** 2)
                a = 2 * (area / 2) - base
                final.append(250 - a)
                final.append(0)
        print(final)
main(3, 1)