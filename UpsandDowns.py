def main(l, n, m, stocks):
    peak_counter_up = 1
    peak_counter_down = n - 1
    valley_counter_up = 1
    valley_counter_down = m - 1
    valleys = 0
    peaks = 0
    valley_down_flag = 0
    valley_up_flag = 0
    peak_down_flag = 0
    peak_up_flag = 0
    no_peaks = 0
    no_valley = 0
    ind_v = 0
    ind_p = 0
    ind = 0
    for i in range(1, len(stocks)):
        if stocks[i] > stocks[i - 1]:
            if valleys != 0 and ind_v == i - 1:
                if valley_counter_down == 0:
                    valley_down_flag = 1
                if peak_up_flag == 1 and peak_counter_down == 0:
                    no_peaks += 1
                peak_counter_up = 1
                valley_counter_up = 1
                peak_up_flag = 0
                peaks = 0
            peak_counter_up += 1
            peaks = stocks[i]
            ind_p = i
            valley_counter_up += 1
        if stocks[i] < stocks[i - 1]:
            if peaks != 0 and ind_p == i - 1:
                if peak_counter_up >= n:
                    peak_up_flag = 1
                if valley_counter_up >= m and valley_down_flag == 1:
                    no_valley += 1
                valley_counter_down = m - 1
                peak_counter_down = n - 1
                valley_down_flag = 0
                valleys = 0
            if valley_counter_down > 0:
                valley_counter_down -= 1
            valleys = stocks[i]
            ind_v = i
            if peak_counter_down > 0:
                peak_counter_down -= 1
    
    if peak_up_flag == 1 and peak_counter_down == 0:
        no_peaks += 1
    if valley_counter_up >= m and valley_down_flag == 1:
        no_valley += 1
    print(no_peaks, ' ', no_valley)
    

l = [4]
n = 2
m = 3
stocks = [1, 3, 2, 4]
main(l, n, m, stocks)
