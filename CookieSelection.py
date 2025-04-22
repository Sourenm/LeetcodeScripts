def main():
    orders = open('CookieSelection.txt')
    cookies = []
    for row in orders:
        check = row.strip()
        if check == '#':
            sorted(cookies)
            print(cookies[int(len(cookies) / 2)])
            cookies.pop(int(len(cookies) / 2))
        else:
            cookies.append(int(check))
main()
