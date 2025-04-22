def main(data):
    data = []
    count = []
    price = []
    reach = 2120000000
    
    result_count = []
    result_price = []
    result_ind = []
    for i in range(len(data)):
        count.append(data[i][0])
        price.append(data[i][1])
    while True:
        check = 0
        if len(price) != 0:
            mul_ind = price.index(max(price))
            if reach < price[mul_ind]:
                price[mul_ind] = 0
                count[mul_ind] = 0
            if sum(price) == 0:
                flag = 0
                for i in range(len(result_count)):
                    if reach % result_count[i] == 0:
                        result_price[i] += reach / result_count[i]
                        flag = 1
                        break
                if flag == 1:
                    break
            else:
                if count[mul_ind] > 0:
                    if count[mul_ind] > reach // price[mul_ind]:
                        if reach // price[mul_ind] == 1:
                            result_ind.append(mul_ind)
                            result_price.append(reach)
                            result_count.append(1)
                            break
                        else:
                            check += price[mul_ind] * (reach // price[mul_ind])
                            count[mul_ind] -= (reach // price[mul_ind])
                            result_ind.append(mul_ind)
                            result_price.append(price[mul_ind])
                            result_count.append(reach // price[mul_ind])
                            price[mul_ind] = 0
                            count[mul_ind] = 0
                    else:
                        check += price[mul_ind] * count[mul_ind]
                        result_ind.append(mul_ind)
                        result_price.append(price[mul_ind])
                        result_count.append(count[mul_ind])
                        price[mul_ind] = 0
                        count[mul_ind] = 0
                else:
                    price[mul_ind] = 0
                    count[mul_ind] = 0
                reach -= check
    print(result_price)
    print(result_count)
    print(result_ind)
    print(len(result_price))

data_sample = [
    (3, 5),
    (7, 10),
    (2, 8),
    (1, 4),
    (6, 12),
    (4, 6),
    (5, 7)
]
main(data_sample)
