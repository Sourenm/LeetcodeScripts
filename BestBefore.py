def main(n):
    lst = list(map(int, n.split('/')))
    day = []
    month = []
    year = []
    for i in range(len(lst)):
        if lst[i] > 12 and lst[i] <= 31:
            day.append(lst[i])
            year.append(lst[i])
        elif lst[i] <= 12:
            day.append(lst[i])
            month.append(lst[i])
            year.append(lst[i])
        elif lst[i] > 31:
            year.append(lst[i])
    for i in range(len(day)):
        if year.count(day[i]) > 0:
            year.pop(year.index(day[i]))
    for i in range(len(month)):
        if year.count(month[i]) > 0:
            year.pop(year.index(month[i]))
    final_year = min(year)
    day.pop(day.index(min(month)))
    final_month = min(month)
    final_day = min(day)
    str_year = ''
    str_month = ''
    str_day = ''
    if final_year < 100:
        str_year = '0'
    str_year +=  str(final_year)
    if final_day < 10:
        str_day = '0'
    str_day += str(final_day)
    if final_month < 10:
        str_month = '0'
    str_month += str(final_month)
    
    print(f'2{str_year}-{str_month}-{str_day}')
    

n = "10/25/2022"
main(n)