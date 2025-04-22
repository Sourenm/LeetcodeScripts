def main(a, b):
    while a != 0 and b != 0:
        if a > b:
            print('Yay the Convention!')
            break
        elif a < b:
            print('Left Beehind')
            break
        else:
            print('Undecided')
            break
main(5, 8)
