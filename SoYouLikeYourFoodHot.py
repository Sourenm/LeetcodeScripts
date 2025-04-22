def main(p, p1, p2):
    pizzas = 0
    while True:
        pitas = 0
        check = 0
        while check < p:
            pitas += 1
            check = pizzas * p1 + pitas * p2
        if check == p:
            print(pizzas, ' ', pitas)
            break
        pizzas += 1
main(2, 3, 4)