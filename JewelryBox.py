import math
def main(x, y):
    a1 = (2 * y - 4 * x + math.sqrt((4 * x - 2 * y) ** 2 + 12 * (-1 * (x ** 2) + x * y))) / -6
    a2 = (2 * y - 4 * x - math.sqrt((4 * x - 2 * y) ** 2 + 12 * (-1 * (x ** 2) + x * y))) / -6
    if a1 >= 0 and a1 > a2:
        b = a1 + y - x
        h = (x - a1) / 2
        print('Max Volume is: ', a1 * b * h)
    elif a2 >= 0 and a2 > a1:
        b = a2 + y - x
        h = (x - a2) / 2
        print('Max Volume is: ', a2 * b * h)
    else:
        print('Could Not Calculate!')
x_sample = 2.0
y_sample = 5.0
main(x_sample, y_sample)