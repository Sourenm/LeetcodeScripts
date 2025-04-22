import math
def main(w, g, h, r):
    if g == h:
        min_d = g
    else:
        height = abs(g - h)
        min_d = math.sqrt((height) ** 2 + (w ** 2))
    height_g = g - r
    height_h = h - r
    x = w / 2
    y = w - x
    a = math.sqrt(((height_g ** 2) + (x ** 2)))
    b = math.sqrt(((height_h ** 2) + (y ** 2)))
    max_d = a + b
    print(min_d, ' ', max_d)
w = 10.0
g = 5.0
h = 8.0
r = 2.0
main(w, g, h, r)
