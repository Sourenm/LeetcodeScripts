def main(n, tax_bands, friends):
    for i in range(len(friends)):
        flag = 0
        for j in range(len(tax_bands)):
            if friends[i][0] < tax_bands[j][0]:
                flag = 1
                if friends[i][0] + friends[i][1] < tax_bands[j][0]:
                    print(friends[i][1] / (1 - (tax_bands[j][1] / 100)))
                    break
                elif friends[i][0] + friends[i][1] > tax_bands[j][0]:
                    tax = (tax_bands[j][0] - friends[i][0]) / (1 - (tax_bands[j][1] / 100))
                    if len(tax_bands) > j:
                        for k in range(j + 1, len(tax_bands)):
                            if tax_bands[k][0] != -1:
                                if friends[i][0] + friends[i][1] > tax_bands[k][0]:
                                    tax += (tax_bands[k][0] - tax_bands[k - 1][0]) / (1 - (tax_bands[k][1] / 100))
                                else:
                                    tax += (friends[i][0] + friends[i][1] - tax_bands[k][0]) / (1 - (tax_bands[k][1] / 100))
                            else:
                                tax += (friends[i][0] + friends[i][1] - tax_bands[k - 1][0]) / (1 - (tax_bands[k][1] / 100))
                    print(tax)
                    break
        if flag == 0:
            print((friends[i][1]) / (1 - (tax_bands[-1][1] / 100)))
    

main(3, [(10000.0, 10.0), (20000.0, 15.0), (30000.0, 20.0)], [(5000.0, 2000.0), (15000.0, 5000.0), (25000.0, 8000.0)])
