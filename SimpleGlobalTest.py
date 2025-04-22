from random import randint
def main():
    
    seqs0 = 'CGGTACGT'
    seqs1 = 'TACCGGTT'
    matrix = [[0 for _ in range(9)] for __ in range(9)]
    back = [["" for _ in range(9)] for __ in range(9)]
    a = 2
    b = 3
    gapo = 4
    gape = 1
    gapo2 = 5
    gape2 = 2
    
    x = 0
    
    score_x_gap = 0
    score_y_gap = 0
    gap_open_y = 0
    gap_open_x = 0
    gap_index_x = 0
    gap_index_y = 0
    # Calculate the scores:
    for i in range(8):
        for j in range(8):
            if seqs0[i] == seqs1[j]:
                miss_match_flag = 1
                score_match_mismatch = matrix[i][j] + a
            else:
                miss_match_flag = 0
                score_match_mismatch = matrix[i][j] - b
            #score_y_gap = matrix[i][j + 1] - (gapo2 + ((j - gap_index_y) * gape2))
            score_y_gap = matrix[i][j + 1] - gapo2
            #score_x_gap = matrix[i + 1][j] - (gapo + ((i - gap_index_x) * gape))
            score_x_gap = matrix[i + 1][j] - gapo
            if score_match_mismatch >= score_y_gap:
                if score_match_mismatch >= score_x_gap:
                    matrix[i + 1][j + 1] = score_match_mismatch
                    back[i + 1][j + 1] = "M"
                    gap_open_y = 0
                    gap_open_x = 0
                    gap_index_x = i
                    gap_index_y = j
                else:
                    if gap_open_x != 1:
                        gap_open_x = 1
                        gap_index_x = i
                    matrix[i + 1][j + 1] = score_x_gap
                    back[i + 1][j + 1] = "I"
            else:
                if score_y_gap > score_x_gap:
                    if gap_open_y != 1:
                        gap_open_y = 1
                        gap_index_y = j
                    matrix[i + 1][j + 1] = score_y_gap
                    back[i + 1][j + 1] = "D"
                else:
                    if gap_open_x != 1:
                        gap_open_x = 1
                        gap_index_x = i
                    matrix[i + 1][j + 1] = score_x_gap
                    back[i + 1][j + 1] = "I"
    for i in range(len(matrix)):
        print(matrix[i])
        #print(back[i])
    
    

main()