def main(Day, Month):
    if Month <= 6:
        actual_day = (Month - 1) * 31 + Day
    else:
        actual_day = 186 + (Month - 7) * 30 + Day
    if actual_day % 7 == 1:
        print('It Was a Sunday!')
    elif actual_day % 7 == 2:
        print('It Was a Monday!')
    elif actual_day % 7 == 3:
        print('It Was a Tuesday!')
    if actual_day % 7 == 4:
        print('It Was a Wednesday!')
    if actual_day % 7 == 5:
        print('It Was a Thursday!')
    if actual_day % 7 == 6:
        print('It Was a Friday!')
    if actual_day % 7 == 0:
        print('It Was a Saturday!')
main(3, 5)