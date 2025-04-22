def main(n):
    vl = 1
    i = 0
    while n > 0:
        n -= vl
        vl *= 2
        n *= 2
        i += 1
        print('Minute :', i)
        print('No of Viruses: ', vl)
        print('No of Bacteria: ', n)
    
    

main(3)